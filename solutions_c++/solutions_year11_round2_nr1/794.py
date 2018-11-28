#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main() {
int t, n;
int cas = 1;
char ch;
scanf("%d", &t);
while(t--) {
scanf("%d", &n);
vector<vector<int> > v(n, vector<int>(n, 0));

scanf("%c", &ch);
for(int i =0;i<n;i++){
for(int j =0; j < n; j++) {
scanf("%c", &ch);
if(ch=='1')
v[i][j] = 1;
else if(ch=='0')
v[i][j] = 0;
else
v[i][j] = -1;
}
scanf("%c", &ch);	//for /n;
}
/*cout<<"input"<<endl;
for(int i=0;i<n;i++){
for(int j =0;j<n;j++)
cout<<v[i][j];
cout<<endl;
}*/
vector<double> wp(n,0), owp(n,0), oowp(n,0);
for(int i =0;i<n;i++) {
double tot = 0;
double win = 0;
for(int j =0;j<n;j++) {
if(v[i][j]!=-1)
tot++;
if(v[i][j]==1)
win++;
}
wp[i] = win/tot;
}

for(int i =0;i<n;i++) {
double sum = 0;
double tempn = 0;
vector<float> temp(n, -1);
for(int k =0;k<n;k++) {
if(k!=i&&v[i][k]!=-1){
	double tot = 0;
	double win = 0;
	for(int j =0;j<n;j++) {
	if(j!=i){
	if(v[k][j]!=-1)
	tot++;
	if(v[k][j]==1)
	win++;
	}
	}
	temp[k] = win/tot;
}
}
for(int k =0;k<n;k++) {
if(temp[k]!=-1) {
sum+=temp[k];
tempn++;
}
}
sum=sum/tempn;
owp[i] = sum;
}
for(int i =0;i<n;i++) {
double tempn = 0;
double sum = 0;
	for(int j =0;j<n;j++) {
		if(v[i][j]!=-1) {
			sum+=owp[j];
			tempn++;
		}	
	}
oowp[i] = sum/tempn;
}
printf("Case #%d:\n", cas++);
for(int i =0;i<n;i++) {
double ans = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
//cout<<ans<<endl;
printf("%lf\n", ans);
}
}
}
