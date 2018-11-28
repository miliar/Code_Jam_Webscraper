#include<fstream.h>                //------------------------------------------------------------//
#include<stdio.h>                  //  ___  ___ _____ ______                                     //
#include<algorithm>                //  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //
#include<math.h>                   //  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
#include<vector.h>                 //  | |\/| | `--. \| ___ \                                    //
#include<set.h>                    //  | |  | |/\__/ /| |_/ /    Email: manish05@facebook.com    //
#include<map.h>                    //  \_|  |_/\____/ \____/                                     //
#include<string.h>                 //------------------------------------------------------------//

         

#define gc getchar_unlocked
#define MEM(a,b) memset(a,(b),sizeof(a))
#define FOR(i,n) for(int i=(0);i<(n);i++)
#define CLEAR(a) memset((a),0,sizeof(a))
#define S(n) scanf("%d", &n)
#define P(k) printf("%d\n", k)
#define fastS(n) scanint(&n)
#define pb push_back
#define mp make_pair
#define ll long long
#define VI vector<int>
#define PII pair<int, int>
#define ft first
#define sd second
#define inf (1<<30)
#define PNL printf("\n")
#define SP system("pause")
#define md 1000000007
#define PII pair<int, int>
#define mxx 1000000000
#define swap(a,b) {*b = (*a + *b) - (*a = *b);}

/*
0-- O won
1-- X won
2-- Draw
3-- Game has not completed
*/
char game[4][5],result[][50]={"O won","X won","Draw","Game has not completed"};
int res[4];

int checkdiagonal(char ch)
{
int flag=1,t=0;
 for(int i=0;i<4;i++)
 {
    if(game[i][i]!=ch)
    {
     if(game[i][i]=='T')
     { 	if(t==0)t++;
      		else
         {
          flag=0;
          break;
         }
     }
     else
     {
     	flag=0;
     	break;
     }
    }
 }

 if(flag) return 1;

 flag=1,t=0;
 for(int i=0;i<4;i++)
 {
    if(game[i][3-i]!=ch)
    {
     if(game[i][3-i]=='T')
     { 	if(t==0)t++;
      		else
         {
          flag=0;
          break;
         }
     }
     else
     {
     	flag=0;
     	break;
     }
    }
 }

 if(flag) return 1;

 return 0;


}

int checkrow(char ch)
{
 for(int i=0;i<4;i++)
 {
 int flag=1,t=0;

 for(int j=0;j<4;j++)
 {
    if(game[i][j]!=ch)
    {
     if(game[i][j]=='T')
     { 	if(t==0)t++;
      		else
         {
          flag=0;
          break;
         }
     }
     else
     {
     	flag=0;
     	break;
     }
    }
 }
 if(flag) return 1;
 }

 return 0;
}

int checkcol(char ch)
{
 for(int i=0;i<4;i++)
 {
 int flag=1,t=0;

 for(int j=0;j<4;j++)
 {
    if(game[j][i]!=ch)
    {
     if(game[j][i]=='T')
     { 	if(t==0)t++;
      		else
         {
          flag=0;
          break;
         }
     }
     else
     {
     	flag=0;
     	break;
     }
    }
 }
 if(flag) return 1;
 }

 return 0;
}

int main()
{
ifstream fin;fin.open("data.in",ios::in);
ofstream fout;fout.open("data.out",ios::out);
	int t;
		fin>>t;

			for(int z=0;z<t;z++)
			{

         FOR(i,4)res[i]=0;

         FOR(i,4)fin>>game[i];

         int draw=1;
         FOR(i,4)
         FOR(j,4)
         if(game[i][j]=='.')
         {
         draw=0;
         res[3]=1;
         }

         if(draw)res[2]=1;

         if(checkdiagonal('O')==1)
         res[0]=1;
         else if(checkdiagonal('X')==1)
         res[1]=1;

			if(checkrow('O')==1)
         res[0]=1;
         else if(checkrow('X')==1)
         res[1]=1;

			if(checkcol('O')==1)
         res[0]=1;
         else if(checkcol('X')==1)
         res[1]=1;

         FOR(i,4)
         {
         	if(res[i])
				{
         		fout<<"Case #"<<(z+1)<<": "<<result[i]<<endl;
         		break;
         	}
			}

         }

    return 0;
}