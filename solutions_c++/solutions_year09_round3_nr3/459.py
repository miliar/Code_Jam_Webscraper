#include <iostream>
#include <vector>
#include <map>
#include <queue>

using std::string;
using std::vector;
using std::map;
using std::queue;
using std::pair;


int calcCost(int p, vector<int> order) {
	
/*	std::cout << "*";
	for (int i = 0; i < order.size(); i++) {
		std::cout << order[i] << " ";
	}*/
	
	int result = 0;
	vector<bool> cellFull(p, true);
	for (int i = 0; i < order.size(); i++) {
		cellFull[order[i]] = false;
		int marker = order[i] - 1;
		while ((marker >=0) && (cellFull[marker])) {
			result++;
			marker--;
		}
		marker = order[i] + 1;
		while ((marker < p) && (cellFull[marker])) {
			result++;
			marker++;
		}
	}
//	std::cout << "result=" << result << std::endl;
	return result;
}


int minCost(int p, vector<int> releases, vector<bool> released, vector<int> order, int left) {
	
/*	std::cout << "*";
	for (int i = 0; i < order.size(); i++) {
		std::cout << order[i] << " ";
	}
	std::cout << std::endl;*/
	
	int result = -1;
	if (left == 0) {
		int tempResult = calcCost(p, order);
		if ((result == -1) || (tempResult < result)) {
			result = tempResult;
		}
	} else {
		for (int i = 0; i < releases.size(); i++) {
			if (!released[i]) {
				released[i] = true;
				order.push_back(releases[i]);
				int tempResult = minCost(p, releases, released, order, left-1);
				order.pop_back();
				released[i] = false;
				if ((result == -1) || (tempResult < result)) {
					result = tempResult;
				}
			}
		}
	}
	
	return result;
}
	

int calcMinCost(int p, const vector<int>& releases) {
	
	vector<int> order;
	vector<bool> released(releases.size(), false);
	return minCost(p, releases, released, order, releases.size());
}


int main()  {
	
	int n;
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		int p, q;
		std::cin >> p >> q;
		vector<int> releases;
		for (int j = 0; j < q; j++) {
			int release;
			std::cin >> release;
			releases.push_back(release-1);
		}
		try {
			std::cout << "Case #" << i+1 << ": " << calcMinCost(p, releases) << std::endl;
		} catch (string& str) {
			std::cout << str << std::endl;
		}
	}			
		
	return 0;
}

