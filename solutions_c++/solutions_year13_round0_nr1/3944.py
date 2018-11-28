// -*- compile-command:"cd c:/MinGW/bin && g++.exe -std=c++11 c:/Users/Josef/Desktop/gcj/tttt.cc -o c:/Users/Josef/Desktop/gcj/t && c:/Users/Josef/Desktop/gcj/t < tomak.in" -*-
#include <iostream>
#include <algorithm>
#include <array>

int xy(int x, int y) { return 4*x + y; }

int main() {

    std::vector<std::array<int, 4> > indices;
    {
      std::array<int, 4> arr;
      for (int i=0; i<4; ++i)
	arr[i] = xy(i, i);
      indices.push_back(arr);

      for (int i=0; i<4; ++i)
	arr[i] = xy(i, 3-i);
      indices.push_back(arr);
    }

    for (int i=0; i<4; ++i) {
      std::array<int, 4> arr;
      for (int j=0; j<4; ++j)
	arr[j] = xy(i, j);
      indices.push_back(arr);

      for (int j=0; j<4; ++j)
	arr[j] = xy(j, i);
      indices.push_back(arr);
    }

    int n; std::cin >> n;

    for (int case_=1; case_<=n; ++case_) {
      char g[4*4];
      for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
          std::cin >> g[xy(i, j)];

      char state = '\0';

      for (auto& arr : indices) {
	int cnt[256] = {};
	for (int i : arr)
	  cnt[(unsigned char)g[i]]++;
	if (cnt[(unsigned char)'T'] +
	    cnt[(unsigned char)'X'] == 4)
	  state = 'X';
	if (cnt[(unsigned char)'T'] +
	    cnt[(unsigned char)'O'] == 4)
	  state = 'O';
      }
      
      std::cout << "Case #" << case_ << ": ";
      if (state) {
        std::cout << state << " won\n";
        continue;
      }
      if (std::count(g, g + sizeof(g)/sizeof(*g), '.') > 0)
        std::cout << "Game has not completed\n";
      else
        std::cout << "Draw\n";
    }
}
