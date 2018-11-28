#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <set>

#define rei(i,a,b) for(int i=a;i<b;i++)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define pb(a,x) a.push_back(x)
#define sort(v) sort(v.begin(),v.end())

using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	map<char,string> h;  
	h['0']="0000";h['1']="0001";h['2']="0010";h['3']="0011";h['4']="0100";h['5']="0101";h['6']="0110";h['7']="0111";h['8']="1000";h['9']="1001";h['A']="1010";h['B']="1011";h['C']="1100";h['D']="1101";h['E']="1110";h['F']="1111";
	rei(t,0,T){
		int M,N;
		cin>>M>>N;
		N/=4;
		vector<string> board;
		rei(i,0,M){
			string tmp="";
			pb(board,tmp);	
			rei(j,0,N){
				char s;
				cin>>s;
				board[i]+=h[s];
			}
		}
		vector<vector<bool> > u(board.size(),vector<bool>(board[0].size(),false));
		int s=(int)min(board.size(),board[0].size());
		vector<vector<int> > ret;
		red(S,s,1){
			vector<int> tp(2,0);
			tp[0]=S;
			tp[1]=0;
			ree(i,0,board.size()-S){
				ree(j,0,board[i].size()-S){
					char color='0';
					bool isP=true;
					rei(x,i,i+S){
						rei(y,j,j+S){
							if(u[x][y]){
								isP=false;
								break;
							}
							if(x==i && y==j){
								color=board[x][y];
								continue;
							}
							if(x!=i && y==j){
								if(S%2==0){
									if(color!=board[x][y]){
										isP=false;
										break;
									}
								}else{
									if(color==board[x][y]){
										isP=false;
										break;
									}else{
										color=board[x][y];
									}	
								}
								continue;
							}
							if(board[x][y]!=color)
								color=board[x][y];
							else{
								isP=false;
								break;
							}
						}
						if(!isP)
							break;
					}
					if(isP){
						tp[1]++;
						rei(x,i,i+S)
							rei(y,j,j+S)
								u[x][y]=true;
					}
				}
			}
			pb(ret,tp);
		}
		int cnt=0;
		rei(i,0,ret.size()){
			if(ret[i][1]!=0)
				cnt++;
		}
		cout<<"Case #"<<t+1<<": "<<cnt<<endl;
		rei(i,0,ret.size()){
			if(ret[i][1]!=0)
				cout<<ret[i][0]<<" "<<ret[i][1]<<endl;
		}
	}
	return 0;
}
