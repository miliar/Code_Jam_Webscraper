#include<iostream>

#define MAX 102
#define INFINITE 10000000
#define T(a,b) Table[a][b]
#define S(a,b) Sign[a][b]

#define MIN(a,b) ((a) > (b)) ? (b) : (a)
#define Control(a,b) ((a)>=0 && (a)<H && (b)>=0 && (b)<W)

#define FOR(a,b) for(int a=0; a<b; a++)

using namespace std;

int H,W;
int Table[MAX][MAX];
int Sign[MAX][MAX];
int Seq[MAX*MAX];
char Alpha[MAX*MAX];
int K=1;

char Edit(int k)	
	{
	if(Seq[k])
		return Alpha[k]=Edit(Seq[k]);
	else
		return Alpha[k];
	}

void Clear()
	{
	FOR(i,K){ Seq[i]=0; Alpha[i]=0; }
	FOR(i,H)FOR(j,W)S(i,j)=0;
	K=1;
	}

void yaz()
	{
	FOR(i,H){FOR(j,W)printf("%d ",S(i,j)); printf("\n");}
	}

void solveProblem()
	{
	int min,minj,t;
	int x,y;
	int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
	
	Clear();
	
	FOR(i,H)
		FOR(j,W)
			{//yaz();
			min=INFINITE;
			minj=0;	
			FOR(k,4)	
				{
				x=i+dir[k][0]; y=j+dir[k][1];
				if(Control(x,y)) 
					{ 
					t=T(x,y);
					if(min>t)
						{
						min=t;
						minj=k;
						}						
					}
				}		
					
			//	printf("min = %d\n",min);
			if(min>=T(i,j))
				{
				if(!S(i,j))
					S(i,j)=K++;
				}
				
			else
				{
				x=i+dir[minj][0];
				y=j+dir[minj][1];
				
				if(!S(i,j))
					{
					if(!S(x,y)) 
						S(x,y)=K++;
					S(i,j) = S(x,y);
					}
				
				else
					{
					if(S(x,y))
						{
						if(S(i,j)!=S(x,y))
							{
							if((Seq[S(i,j)]!=0 && Seq[S(i,j)]<S(x,y)))
								Seq[S(x,y)]=S(i,j);
							else if((Seq[S(x,y)]!=0 && Seq[S(x,y)]<S(i,j)))
								Seq[S(i,j)]=S(x,y);							 
							else if(S(i,j)<S(x,y))
								Seq[S(x,y)]=S(i,j);
							else 
								Seq[S(i,j)]=S(x,y);
							}
						}
						
					else
						S(x,y) = S(i,j);
					}
				}	
			
		//	FOR(i,K)printf("%d ",Seq[i]);printf("\n");
			}
		
	t='a'-1;
	Alpha[0]=-t;
	FOR(i,K)
		if(!Seq[i])
			Alpha[i]=t++;
	
	FOR(i,K)
		if(Seq[i])
			Edit(i);
	}

void writeProblem()
	{
	FOR(i,H){ FOR(j,W) printf("%c ",Alpha[S(i,j)]); printf("\n");}
	}

int main()
	{
	int t;
	cin>>t;
	
	FOR(k,t)
		{
		cin>>H>>W;
		FOR(i,H)FOR(j,W)cin>>T(i,j);
		
		cout<<"Case #"<<k+1<<": "<<endl;
		solveProblem();	
		writeProblem();
		}
	return 0;
	}
