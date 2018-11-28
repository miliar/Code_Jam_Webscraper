#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i = 0;i<T;i++)
	{
		int H, W;
		cin>>H;
		cin>>W;
		std::vector<int> mapa(W*H);
		for (int y=0;y<H;++y) {
			for (int x=0;x<W;++x) {
				cin >> mapa[y*W + x];
			}
		}

		int new_label = 0;
		std::vector<int> mapl(W*H, -1);
		for (int y=0;y<H;++y) {
			for (int x=0;x<W;++x) {
				int pos=y*W + x;
				int flow=0;
				if (y>0 && mapa[pos-W] < mapa[pos+flow]) flow = -W;
				if (x>0 && mapa[pos-1] < mapa[pos+flow]) flow = -1;
				if (x<W-1 && mapa[pos+1] < mapa[pos+flow]) flow = 1;
				if (y<H-1 && mapa[pos+W] < mapa[pos+flow]) flow = W;

				if (flow == 0) {
					if (mapl[pos] == -1) mapl[pos] = new_label++;
				} else {
					if (mapl[pos] == -1 && mapl[pos+flow] == -1) {
						mapl[pos] = mapl[pos+flow] = new_label++;
					} else if (mapl[pos] != -1 && mapl[pos+flow] == -1) {
						mapl[pos+flow] = mapl[pos];
					} else if (mapl[pos] == -1 && mapl[pos+flow] != -1) {
						mapl[pos] = mapl[pos+flow];
					} else {
						int merge_from = mapl[pos+flow];
						int merge_to = mapl[pos];
						new_label = 0;
						std::vector<int> table;
						table.reserve(26);
						for (int yy=0;yy<H;++yy) {
							for (int xx=0;xx<W;++xx) {
								int old = mapl[yy*W + xx];
								if (old == merge_from) old = merge_to;
								if (old != -1) {
									if (table.size() <= old) table.resize(old + 1, -1);
									if (table[old] == -1) table[old] = new_label++;
									mapl[yy*W + xx] = table[old];
								}
							}
						}

					}
				}
			}
		}

		printf("Case #%d:\n", i+1);
		for (int y=0;y<H;++y) {
			for (int x=0;x<W;++x) {
				putchar('a' + mapl[y*W + x]);
				putchar(x+1<W ? ' ' : '\n');
			}
		}
	}

	return 0;
}
