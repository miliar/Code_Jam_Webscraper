#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");

char sq[20][20];
int sqv[20][20];

bool done[20][20][20000];
int bests[20][20][20000];

int px[4]={0,1,0,-1};
int py[4]={1,0,-1,0};

int dolis[10000000][3];

int mod = 10000;
bool isq[251];

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	getline(cin,s);
	int ax,ay,bx,by,cx,cy;
	int w;
	int q;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		vector<string> anses;
		string empt;
		cin >> w >> q;
		int readfrom=0;
		int writeto= 0;
		int tot =0;
		memset(done,0,sizeof(done));
		memset(bests,0,sizeof(done));
		memset(isq,0,sizeof(isq));
		for(i=0; i<w; i++)
		{
			for(j=0; j<w; j++)
			{
				cin >> sq[i][j];
				if('0'<=sq[i][j] && sq[i][j]<='9')
				{
					sqv[i][j]=(sq[i][j]-'0');
					done[i][j][(sq[i][j]-'0')+mod]=true;
					bests[i][j][(sq[i][j]-'0')+mod]=writeto;
					dolis[writeto][0]=i;
					dolis[writeto][1]=j;
					dolis[writeto][2]=(sq[i][j]-'0')+mod;
					string t(1,sq[i][j]);
					anses.push_back(t);
					//cout << anses[writeto] << " "  << sq[i][j] <<endl;
					writeto++;
				}
			}
		}
		vector <int> quer;
		k=0;
		for(i=0; i<q; i++)
		{
			cin >> j;
			quer.push_back(j);
			if(isq[j]==true)
				k++;
			isq[j]=true;
		}
		q-=k;
		
		int lastsz = 1;
		for(i=0; i<writeto; i++)
		{
			j=dolis[writeto][2]-mod;
			if(j<=0 || j>250)
				continue;
			if(isq[j])
			{
				q--;
				isq[j]=false;
			}
		}
		
		while(readfrom<writeto)
		{
			cx = dolis[readfrom][0];
			cy = dolis[readfrom][1];
			tot = dolis[readfrom][2];
			//fout << cx << " " << cy << " " << tot << " " << anses[readfrom] << endl;
			if(bests[cx][cy][tot]!=readfrom)
			{
				readfrom++;
				continue;
			}
			if(q==0 && anses[bests[cx][cy][tot]].size()>lastsz)
				break;
			
			for(i=0; i<4; i++)
			{
				bx=cx+px[i];
				by=cy+py[i];
				if(0>bx || bx>=w || 0>by || by>=w)
					continue;
				
				for(j=0; j<4; j++)
				{
					ax=bx+px[j];
					ay=by+py[j];
					if(0>ax || ax>=w || 0>ay || ay>=w)
						continue;
					if(sq[bx][by]=='+')
					{
						k=tot+sqv[ax][ay];
					}
					else
					{
						k=tot-sqv[ax][ay];
					}
					if(k>=2*mod || k<0)
						continue;
					string tt = (((anses[readfrom]+sq[bx][by])+sq[ax][ay]));
					//fout << tt << " " << anses[bests[ax][ay][k]] << " ";
					if((!done[ax][ay][k] || (tt.size()<anses[bests[ax][ay][k]].size())) || ((tt.size()==anses[bests[ax][ay][k]].size())&&(tt<anses[bests[ax][ay][k]])))
					{
						//fout << "IN" << endl;
						bests[ax][ay][k]=writeto;
						done[ax][ay][k]=true;
						anses.push_back((((anses[readfrom]+sq[bx][by])+sq[ax][ay])));
						dolis[writeto][2]=k;
						dolis[writeto][0]=ax;
						dolis[writeto][1]=ay;
						int l = k-mod;
						if(0<=l && l<=250 && isq[l])
						{
							//cout << "SOLVE " << l << " " << anses[writeto] << endl;
							isq[l]=false;
							q--;
							lastsz=anses[writeto].size();
							
						}
						writeto++;
					}
					else
					{
						//fout << "OUT" << endl;
					}
				}
			}
			readfrom++;
		}
		
		
		
		cout << "Case #" << ct << ":" <<endl;
		fout << "Case #" << ct << ":" << endl;
		int ansx,ansy;
		for(i=0; i<quer.size(); i++)
		{
			ansx=ansy=-1;
			for(j=0; j<w; j++)
			{
				for(k=0; k<w; k++)
				{
					if(!done[j][k][quer[i]+mod])
						continue;
					//cout<< anses[bests[j][k][quer[i]+mod]] << " " << quer[i] << endl;
					if(ansx==-1)
					{
						ansx=j;
						ansy=k;
					}
					else if(anses[bests[ansx][ansy][quer[i]+mod]].size() >anses[bests[j][k][quer[i]+mod]].size())
					{
						ansx=j;
						ansy=k;
					}
					else if((anses[bests[ansx][ansy][quer[i]+mod]].size() == anses[bests[j][k][quer[i]+mod]].size())&&(anses[bests[ansx][ansy][quer[i]+mod]] >anses[bests[j][k][quer[i]+mod]]))
					{
						ansx=j;
						ansy=k;
					}
				}
			}
			cout << anses[bests[ansx][ansy][quer[i]+mod]] << endl;
			fout << anses[bests[ansx][ansy][quer[i]+mod]] << endl;
		}
		anses.clear();
		
	}

	
	return 0;
}

