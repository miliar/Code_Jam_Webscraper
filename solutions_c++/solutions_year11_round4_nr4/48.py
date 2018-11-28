#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>
#include <queue>

typedef unsigned int uint;

struct TestInput {
	std::vector<std::vector<uint> > edges;
};

struct TestOutput {
	uint conquered, threatened;
};

struct Path {
	uint dist;
	uint threatened;
	uint last, prev;
	Path(uint dist, uint last, uint prev, uint threatened): dist(dist), last(last), prev(prev), threatened(threatened) { }
/*	bool operator<(const Path &p) const {
		return std::make_pair(last, prev)<std::make_pair(p.last, p.prev);
	}*/
	Path move(uint next) const {
		return Path(dist+1, next, last, threatened);
	}
};

static TestOutput runTest(const TestInput &in) {
	uint n = (uint)in.edges.size();
	TestOutput res;
	res.conquered = n+1;
	res.threatened = 0;
	std::vector<std::vector<bool> > adj(n, std::vector<bool>(n, false));
	std::vector<uint> dist(n, (uint)-1);
	{
		std::queue<uint> q;
		q.push(1);
		dist[1] = 0;
		while (!q.empty()) {
			uint c = q.front(); q.pop();
			for (uint i=0; i<in.edges[c].size(); i++) {
				uint next = in.edges[c][i];
				if (dist[next]==(uint)-1) {
					dist[next] = dist[c] + 1;
					q.push(next);
				}
			}
		}
	}

	for (uint i=0; i<n; i++)
		for (uint j=0; j<in.edges[i].size(); j++)
			adj[i][in.edges[i][j]] = true;
	if (adj[0][1]) {
		res.conquered = 0;
		res.threatened = in.edges[0].size();
		return res;
	}
	std::vector<std::vector<uint> > maxThreats(n, std::vector<uint>(n, 0));
	std::queue<Path> q;
	for (uint i=0; i<in.edges[0].size(); i++) {
		uint next = in.edges[0][i];
		if (dist[next]!=dist[0]-1)
			continue;
		Path p(1, next, 0, 0);
		for (uint j=0; j<n; j++)
			if (adj[0][j] || adj[next][j])
				p.threatened++;
		maxThreats[p.last][p.prev] = p.threatened;
		q.push(p);
	}
	while (!q.empty()) {
		Path p = q.front();
		q.pop();
		if (maxThreats[p.last][p.prev]!=p.threatened)
			continue;

		for (uint j=0; j<in.edges[p.last].size(); j++) {
			uint next = in.edges[p.last][j];
			if (dist[next]!=dist[p.last]-1)
				continue;

			if (next==1) {
				if (p.threatened>res.threatened)
					res.threatened = p.threatened;
				continue;
			}

			Path newPath = p.move(next);
			for (int k=0; k<in.edges[next].size(); k++) {
				uint th = in.edges[next][k];
				if ((!adj[p.last][th]) && (!adj[p.prev][th]))
					newPath.threatened++;
			}
			if (newPath.threatened>maxThreats[newPath.last][newPath.prev]) {
				q.push(newPath);
				maxThreats[newPath.last][newPath.prev] = newPath.threatened;
			}
		}
	}
	res.conquered = dist[0] - 1;
	res.threatened -= res.conquered+1;
	return res;
}

static void readEx() {
	throw std::runtime_error("error reading input");
}

static void writeEx() {
	throw std::runtime_error("error reading input");
}

static std::istream &operator>>(std::istream &fi, TestInput &in) {
	uint P, W;
	fi >> P >> W;
	in.edges.resize(P);
	for (uint i=0; i<W; i++) {
		uint x, y;
		char c;
		fi >> x >> c >> y;
		if (c!=',' || fi.fail())
			readEx();
		in.edges[x].push_back(y);
		in.edges[y].push_back(x);
	}
	return fi;
}

static std::ostream &operator<<(std::ostream &fo, const TestOutput &out) {
	fo << out.conquered << ' ' << out.threatened;
	return fo;
}

static std::vector<TestInput> readInput(const char *filename) {
	std::ifstream fi(filename);
	std::string testCountS;
	std::getline(fi, testCountS);
	if (fi.fail())
		readEx();
	uint testCount;
	std::istringstream testCountSt(testCountS);
	testCountSt >> testCount;
	if (testCountSt.fail())
		readEx();
	std::vector<TestInput> res(testCount);
	for (uint i=0; i<testCount; i++)
		fi >> res[i];
	return res;
}

static void writeOutput(const char *filename, const std::vector<TestOutput> &output) {
	std::ofstream fo(filename);
	if (fo.fail())
		writeEx();
	for (uint i=0; i<output.size(); i++) {
		fo << "Case #" << (i+1) << ": " << output[i] << std::endl;
		if (fo.fail())
			writeEx();
	}
}

int main(int argc, const char **argv) {

	try {
		const char *inFilename = argc>=2 ? argv[1] : "in";
		const char *outFilename = argc>=3 ? argv[2] : "out";

		std::vector<TestInput> in = readInput(inFilename);
		std::vector<TestOutput> out(in.size());
		for (unsigned int i=0; i<in.size(); i++) {
			out[i] = runTest(in[i]);
			std::cerr << '\r' << (i+1) << "/" << in.size();
			std::cerr.flush();
		}
		std::cerr << std::endl;
		writeOutput(outFilename, out);
	} catch (const std::exception &ex) {
		std::cerr << "exception: " << ex.what() << std::endl;
		return 1;
	}
	return 0;
}
