#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//struct score
//{
//	int x,y,z;
//	//int type;
//	//bool ok;
//	score(const int a,const int b,const int c/*,const int t,const bool k*/)
//		  :x(a),y(b),z(c)/*,type(t),ok(k)*/{}
//};

int n,s,p;
int Res;
//vector<score> Googler;

//bool cmp(const score& ls,const score& rs)
//{
//	return ls.type < rs.type;
//}

int main()
{
	FILE *in,*out;
	in = freopen("B-large.in","r",stdin);
	out = freopen("B-small-attempt0.txt","w",stdout);
	int TCases;
	int NCase = 1;
	cin >>TCases;
	while(TCases--)
	{
		//Googler.clear();
		Res = 0;
		cin >>n >>s >>p;
		//cout <<n <<' '<<s <<' ' <<p <<' ';
		int N_Nop = n;
		for(int i = 0;i < n;i++)
		{
			int Temp;
			/*bool Ok;
			Ok = false;*/
			cin >>Temp;  //cout <<Temp <<' ';
			int Base = Temp/3;
			
			switch(Temp%3)
			{
			case 0:
				{
					/*if(Base+1 >= p && Temp >= 3)
					{
						Ok = true;
						N_Nop--;
						Res++;
					}*/
					if(Base >= p)
					{
						Res++;
					}
					else if(s > 0 && Base > 0 && Base+1 >= p)
					{
						s--;
						Res++;
					}
					//Googler.push_back(score(Base-1,Base,Base+1));
					
					break;
				}
			case 1:
				{
				/*	if(Base+1 >= p && Temp >= 4)
					{
						Ok = true;
						N_Nop--;
						Res++;
					}*/
					if(Base+1 >= p)
					{
						Res++;
					}
					//Googler.push_back(score(Base-1,Base+1,Base+1));
					
					break;
				}
			case 2:
				{	
					/*if(Base+2 >= p)
					{
						Ok = true;
						N_Nop--;
						Res++;
					}*/
					if(Base+1 >= p)
					{
						Res++;
					}
					else if(s > 0 && Base+2 >= p)
					{
						Res++;
						s--;
					}
					//Googler.push_back(score(Base,Base,Base+2));
				
					break;
				}
			default:break;
			}
		}
		
		//sort(Googler.begin(),Googler.end(),cmp);
	/*	int Cut = n-s-N_Nop;
		for(vector<score>::size_type i = 0;i != Googler.size() && Cut > 0;i++)
		{
			if(Googler[i].ok)
			{
				if(0 == Googler[i].type)
				{
					Cut--;
				}
				else
				{
					int Temp = Googler[i].z - 1;
					if(Temp < p)
						Res--;
					Cut--;
				}
			}
		}*/
		
		cout <<"Case #" <<NCase++ <<": " <<Res <<endl;
	}
	fclose(in);
	fclose(out);
	return 0;
}