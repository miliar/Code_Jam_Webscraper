#include <iostream>
#include <string>
#include  <cmath>
#include  <fstream>
#include <vector>
using namespace std;


int main(void)
{
    int i,j;
    vector<int> left;
    vector<int> right;
    ifstream cin("A-large.in");
    ofstream fout("aL.out");
    int a,b,x,y,linenum;
int case_num;
cin>>case_num;
int t=1;
while(case_num--){
    left.clear();
	right.clear();
    fout<<"Case #"<<t<<": ";
    t++;
    cin>>linenum;
    for(i=0;i<linenum;i++){
        cin>>x>>y;
        left.push_back(x);
        right.push_back(y);
    }
    int  count=0;
    for(i=0;i<linenum;i++){
        for(j=i+1;j<linenum;j++){
            if(((left.at(i)-left.at(j))*(right.at(i)-right.at(j)))<0){
                count++;
            }
        }
    }
    fout<<count<<endl;
}
}
