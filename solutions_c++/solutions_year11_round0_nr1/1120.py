#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;
struct button{
    char robot;
    int de;
}r[101];
int main(){
    ifstream fin("A-small-attempt4.in");
    ofstream fout("A-small-attempt4.out");
	int t,n,otime,btime;
	int op,bp;
	fin >> t;
	for(int i = 1;i <= t;i ++){
		op = 1;
		bp = 1;
		otime = 0;
		btime = 0;
		fin >> n;
		for(int j = 0;j < n;j ++){
			fin >> r[j].robot >> r[j].de;
		}
		for(int j = 0;j < n;j ++){
            if(r[j].robot == 'O'){
                otime += (abs(r[j].de - op) + 1);
                int k;
                for(k = j + 1;k < n;k ++){
                    if(r[k].robot == 'B')
                        break;
                }
                if(r[k].de > bp){
                    bp += (abs(r[j].de - op) + 1);
                    if(bp > r[k].de)
                        bp = r[k].de;
                }
                else{
                    bp -= (abs(r[j].de - op) + 1);
                    if(bp < r[k].de)
                        bp = r[k].de;
                }
                op = r[j].de;
            }
            else{
                btime += (abs(r[j].de - bp) + 1);
                int k;
                for(k = j + 1;k < n;k ++){
                    if(r[k].robot == 'O')
                        break;
                }
                if(r[k].de > op){
                    op += (abs(r[j].de - bp) + 1);
                    if(op > r[k].de)
                        op = r[k].de;
                }
                else{
                    op -= (abs(r[j].de - bp) + 1);
                    if(op < r[k].de){
                        op = r[k].de;
                    }
                }
                bp = r[j].de;
            }
		}
		fout << "Case #" << i << ": " << otime + btime << endl;

	}
	return 0;
}
