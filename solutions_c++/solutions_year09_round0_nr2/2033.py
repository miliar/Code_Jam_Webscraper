#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T, t, H, h, w, W, altinc, x, y, z, done, sink;
	char sink_letter;
	char basin[30];
	int altitudes[12000];
	int drains[12000];
	char out[12000];
	int neighbours[10];

	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	myfile >> T;

cout << T;
	for (t=1;t<=T;t++) {
		myfile >> H >> W;
			for (altinc=0;altinc<(H*W);altinc++) {
			myfile >> altitudes[altinc];
		}

		altinc=0;
		sink = 10;
		for (h=0;h<H;h++) {
			for (w=0;w<W;w++) {
				out [((h*W)+w)]=-1;

				if (h==0) neighbours[1]=10000;
				else neighbours[1] = altitudes[(((h-1)*W)+w)];
				if (w==(W-1)) neighbours[3]=10000;
				else neighbours[3] = altitudes[((h*W)+w+1)];
				if (h==(H-1)) neighbours[4]=10000;
				else neighbours[4] = altitudes[(((h+1)*W)+w)];
				if (w==0) neighbours[2]=10000;
				else neighbours[2] = altitudes[((h*W)+w-1)];

				y=10000;
				z=0;
				for (x=1;x<5;x++) {
					if (neighbours[x]<y) {
						y=neighbours[x];
						z=x;
					}
				}

				if (altitudes[((h*W)+w)]>y) drains[((h*W)+w)]=z;
				else {
					drains[((h*W)+w)]=sink;
					sink++;
				}
			}
		}

		done = 0;
		do {
			done = 1;
			for (h=0;h<H;h++) {
				for (w=0;w<W;w++) {
					if (drains[((h*W)+w)]<10) done=0;
					else {
						sink = drains[((h*W)+w)];
						if ((h>0) && (drains[(((h-1)*W)+w)]==4)) drains[(((h-1)*W)+w)]=sink;
						if ((w<(W-1)) && (drains[((h*W)+w+1)]==2)) drains[((h*W)+w+1)]=sink;
						if ((h<(H-1)) && (drains[(((h+1)*W)+w)]==1)) drains[(((h+1)*W)+w)]=sink;
						if ((w>0) && (drains[((h*W)+w-1)]==3)) drains[((h*W)+w-1)]=sink;
					}
				}
			}
		} while (done==0);

		for (z=0;z<28;z++) {
			basin[z]=-1;
		}
		output << "Case #" << t <<":\n";
		cout << t << "\n";
		sink_letter='a';
		for (h=0;h<H;h++) {
			for (w=0;w<W;w++) {
				if (basin[(drains[((h*W)+w)]-10)] == -1) {
					basin[(drains[((h*W)+w)]-10)] = sink_letter;
					sink_letter++;
				}
				out [((h*W)+w)] = basin[(drains[((h*W)+w)]-10)];
				output << out[((h*W)+w)] <<" ";
			}
			output << "\n";
		}
	}
	return 0;
}
