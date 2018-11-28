#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	
	for (int n=1;n<=T;n++) {
		vector<vector<char> > d;
		float k;
		char a;
		cin >> k;
		for (int i=0;i<k;i++) {
			d.push_back(vector<char>());
			for (int j=0;j<i+1;j++) {
				cin >> a;
				d[i-j].push_back(a);
			}
		}
		for (int i=0;i<k;i++) {
			for (int j=k-1;j>i;j--) {
				cin >> a;
				d[j].push_back(a);
			}
		}
		int ans=-1;
		/*for (int i=0;i<k;i++) {
			cout << endl;
			for (int j=0;j<k;j++) {
				cout << d[i][j] << " ";
			}
		}
		cout << endl;*/
		for (float i=-k/2;i<k+k/2;i+=0.5) {
			//for (float j=0+(int(i)==i?0:0.5);j<k-0.5;j+=1) {
			for (float j=0-i;j<k+i;j++) {
				bool bad=false;
				//for (int x=0;x<i;x++) {
					//for (int y=max(0,int(j-(i-x)));y<=min(k-1,int(j+(i-x)));y++) {
				for (int x=0;x<k;x++) {
					for (int y=0;y<k;y++) {
						float a=(i-x)-(j-y);
						float b=(i-x)+(j-y);
						
						int x1=i-(a+b)/2; //=x
						int y1=j-(b-a)/2; //=y
						int x2=i-(-a+b)/2; //=x
						int y2=j-(b+a)/2; //=y
						int x3=i-(a-b)/2; //=x
						int y3=j-((-b)-a)/2; //=y
						int x4=i-((-a)-b)/2; //=x
						int y4=j-((-b)+a)/2; //=y
						if (x2>=0 && x2<k && y2>=0 && y2<k) {
							if (d[x1][y1]!=d[x2][y2]) {bad=true;break;}
						}
						if (x3>=0 && x3<k && y3>=0 && y3<k) {
							if (d[x1][y1]!=d[x3][y3]) {bad=true;break;}
						}
						if (x4>=0 && x4<k && y4>=0 && y4<k) {
							if (d[x1][y1]!=d[x4][y4]) {bad=true;break;}
						}
					}
					if (bad) break;
				}
				if (!bad) {
					int xdiff=abs(int(k-1-2*i));
					int ydiff=abs(int(k-1-2*j));
					int ex=max(xdiff,ydiff);
					if (ans==-1||ans>ex) ans=ex;
				}
				//cout << bad << " ";
			}	
			//cout << endl;
		}
		//cout << ans << endl;
		//if (ans==-1) ans=k-1;
		cout << "Case #" << n << ": " << (k+ans)*(k+ans)-k*k << endl;;
		
	}
	
	return 0;	
}
