#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
 
#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))
 
int main(){
	int test;
	scanf("%d",&test);
	ree(t,1,test){
		printf("Case #%d:\n",t);
		int n;
		scanf("%d",&n);
		vector<string> mat(n,"");
		rei(i,0,n) cin>>mat[i];
		vector<vector<double> > score(n,vector<double>(3,0.));
		vector<int> plyd(n,0);
		vector<int> wn(n,0);
		rei(i,0,n){
			int played=0;
			int won=0;
			rei(j,0,n){
				if(i==j) continue;
				if(mat[i][j]!='.') played++;
				if(mat[i][j]=='1') won++;	
			}
			plyd[i]=played;
			wn[i]=won;
			score[i][0]=won*1./played*1.;
		}
/*		cout<<"WP"<<endl;
		rei(i,0,n){
			cout<<score[i][0]<<endl;
		}
*/		rei(i,0,n){
			double scr=0.;
			rei(j,0,n){
				if(i==j) continue;
				if(mat[i][j]!='.'){
					if(plyd[j]==1){
						scr+=0.;
						continue;
					}
					if(mat[i][j]=='0')
						scr+= ((wn[j]-1.)/(plyd[j]-1.));	
					else
						scr+= ((wn[j])/(plyd[j]-1.));
				}
			}
			scr=scr*1./plyd[i]*1.;
			score[i][1]=scr;
		}
/*		cout<<"OWP"<<endl;
		rei(i,0,n){
			cout<<score[i][1]<<endl;
		}
*/		rei(i,0,n){
                        double scr=0.;
                        rei(j,0,n){
                                if(i==j) continue;
                                if(mat[i][j]!='.'){
                                        scr+=score[j][1];
                                }
                        }
                        scr=scr*1./plyd[i]*1.;
                        score[i][2]=scr;
                }
/*		cout<<"OOWP"<<endl;
		rei(i,0,n)
			cout<<score[i][2]<<endl;
*/		rei(i,0,n){
			double scre=(0.25*score[i][0]) + (0.5*score[i][1]) + (0.25*score[i][2]);
			printf("%.8lf\n",scre);
		}
	}
	return 0;
}
