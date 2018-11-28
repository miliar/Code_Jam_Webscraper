#include <fstream>
#include <iostream>
#include <exception>
#include <string>
#include <memory>
#include <algorithm>

typedef long long ll;

struct Mountain {
	ll height;
	ll slope;
	Mountain *next;
};

bool run(Mountain *first, Mountain *last) {
	for (Mountain *c = first; ; ) {
		if (c==last) break;
		if (c>last) return false;
		if (c->next<=c) return false;
		c->height = last->height + last->slope*(last-c);
		c->slope = last->slope-1;
		c = c->next;
	}
	last->slope--;
	for (Mountain *c = first; c!=last; c=c->next)
		if (!run(c+1, c->next)) return false;
	return true;
}

void run(std::ifstream &fi, std::ofstream &fo) {
	ll n;
	fi >> n;
	std::unique_ptr<Mountain[]> mountains(new Mountain[n]);
	for (ll i=0; i+1<n; i++) {
		ll x;
		fi >> x;
		mountains[i].next = mountains.get()+(x-1);
	}
	mountains[n-1].height = 0;
	mountains[n-1].slope = 0;
	if (!run(mountains.get(), mountains.get()+n-1)) {
		fo << " Impossible";
		return;
	}
	ll min = 0;
	for (ll i=0; i<n; i++)
		min = std::min(min, mountains[i].height);
	for (ll i=0; i<n; i++) {
		ll h = mountains[i].height - min;
		if (h<0 || h>1000000000)
			std::cerr << "wrong height " << h << std::endl;
		fo << ' ' << h;
	}
}

int main(int argc, const char **argv) {
	try {
		unsigned int T;
		std::string inFilename(argc<=1 ? "in" : argv[1]);
		std::string outFilename = inFilename + ".out";
		std::ifstream fi(inFilename);
		fi.exceptions(std::ios::badbit | std::ios::failbit);
		std::ofstream fo(outFilename);
		fo.exceptions(std::ios::badbit | std::ios::failbit);
		fi >> T;
		for (unsigned int t=1; t<=T; t++) {
			fo << "Case #" << t << ":";
			run(fi, fo);
			fo << std::endl;
			std::cout << '\r' << t << '/' << T; std::cout.flush();
		}
		std::cout << std::endl;
	} catch (const std::exception &ex) {
		std::cerr << "\nexception: " << ex.what() << std::endl;
	} catch (...) {
		std::cerr << "\nwhoops\n";
	}
	return 0;
}
