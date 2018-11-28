#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;
FILE *in, *out;

int move[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
int map[210][210];
vector<pair<int, int> > point;

int ccw(double x1, double y1, double x2, double y2, double x3, double y3){
	double ret = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3);
	if(ret > 0) return 1;
	else return -1;
}

bool inside(int rx, int ry){
	double x = double(rx)-0.5;
	double y = double(ry)+0.5;
	double x2 = 213.25;
	double y2 = 225.13;

	int intersect=0;
	for(int i=1;i<point.size();i++){
		if(point[i-1] == point[i]) continue;
		if(ccw(point[i-1].first, point[i-1].second, point[i].first, point[i].second, 
					x, y) * ccw(point[i-1].first, point[i-1].second, 
						point[i].first, point[i].second, x2, y2) != -1) continue;

		if(ccw(x, y, x2, y2, point[i-1].first, point[i-1].second) *
				ccw(x, y, x2, y2, point[i].first, point[i].second) != -1) continue;

		intersect++;
	}
	return (intersect % 2 == 1);
}

int main(){
	in = fopen("A.in", "r");
	out = fopen("A.out", "w");
	int n;
	fscanf(in, "%d", &n);
	for(int t=1;t<=n;t++){
		int dir=0, x=100, y=100;
		point.clear();
		for(int i=0;i<=200;i++)
			for(int j=0;j<=200;j++)
				map[i][j] = 0;

		int T;
		fscanf(in, "%d", &T);
		point.push_back(make_pair(100, 100));
		for(int i=0;i<T;i++){
			char path[18];
			int rep;
			fscanf(in, "%s %d", path, &rep);
			
			for(int k=0;k<rep;k++)
				for(int j=0;j<strlen(path);j++){
					if(path[j] == 'F'){
						x += move[dir][0];
						y += move[dir][1];
					}
					else if(path[j] == 'R'){
						point.push_back(make_pair(x, y));
						dir = (dir+1)%4;
					}
					else if(path[j] == 'L'){
						point.push_back(make_pair(x, y));
						dir = (dir+3)%4;
					}
				}

		}
		point.push_back(make_pair(100, 100));

		for(int i=0;i<=200;i++)
			for(int j=0;j<=200;j++)
				if(inside(i, j)){
					map[i][j] = 1;
				}

		int result=0;
		for(int i=0;i<=200;i++)
			for(int j=0;j<=200;j++){
				if(map[i][j]) continue;
				bool ck=false, ck2=false;
				for(int k=0;k<i && !ck;k++)
					if(map[k][j])
						ck = true;
				for(int k=i+1;k<=200 && !ck2;k++)
					if(map[k][j])
						ck2 = true;
				if(ck && ck2){ result++; continue; }
				ck=false, ck2=false;
				for(int k=0;k<j && !ck;k++)
					if(map[i][k])
						ck = true;
				for(int k=j+1;k<=200 && !ck2;k++)
					if(map[i][k])
						ck2 = true;
				if(ck && ck2) result++;
			}

		fprintf(out, "Case #%d: %d\n", t, result);
	}
	fclose(in);
	fclose(out);
	return 0;
}
