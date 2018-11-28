#include <iostream>
#include <queue>

using namespace std;

int mask[10];
char key[10];

typedef struct  
{
	int state[10][10];
	int step;
}Node;

Node st;
int n;

typedef struct  
{
    int mat[10][10];
    int next;
}Table;

const int MAXN=332000;
const int prime=65535;

Table hash[MAXN];
bool flag[prime+1];

int eid;

bool cmp(int mat1[][10],int mat2[][10])
{
    int i,j;
    
    for (i=0;i<n;++i)
    {
        for (j=0;j<n;++j)
        {
            if (mat1[i][j]!=mat2[i][j])
            {
                return false;
            }
        }
    }
    
    return true;
}

inline void insert(int mat[][10])
{
    int rd;
    int i,j;
    int key=0;

    for (i=0;i<n;++i)
    {
        for (j=0;j<n;++j)
        {
            key+=mat[i][j]*(13-i-j)*(mat[i][j]*i-mat[i][j]*j+i*j);
        }
    }

    while (key<0)
    {
        key+=(prime+1);
    }

    rd=key&prime;

    if (!flag[rd])
    {
        flag[rd]=true;
        for (i=0;i<n;++i)
        {
            for (j=0;j<n;++j)
            {
                hash[rd].mat[i][j]=mat[i][j];
            }
        }    
        hash[rd].next=-1;
        return;
    }
    
    for (i=0;i<n;++i)
    {
        for (j=0;j<n;++j)
        {
            hash[eid].mat[i][j]=mat[i][j];
        }
    }

    hash[eid].next=hash[rd].next;
    hash[rd].next=eid;
    ++eid;    

}

inline int qurey(int mat[][10])
{
    int i,j;
    int key=0;

    for (i=0;i<n;++i)
    {
        for (j=0;j<n;++j)
        {
            key+=mat[i][j]*(13-i-j)*(mat[i][j]*i-mat[i][j]*j+i*j);
        }
    }

    while (key<0)
    {
        key+=(prime+1);
    }

    int rd=key&prime;

    if (!flag[rd])
    {
        return -1;
    }

    while (rd!=-1)
    {
        if (cmp(hash[rd].mat,mat))
        {
            return rd;
        }

        rd=hash[rd].next;
    }

    return -1;
    
}

inline void init()
{
    eid=prime;
    memset(flag,0,sizeof(flag));
}



inline int Bfs()
{
	queue<Node> q;
	
	q.push(st);

	int i,j;


	insert(st.state);	

	while (!q.empty())
	{
		Node t=q.front();
		q.pop();


		bool finish=true;

		for (i=0;i<n;++i)
		{
			for (j=i+1;j<n;++j)
			{
				if (t.state[i][j]==1)
				{
					finish=false;
					break;
				}
			}

			if (!finish)
			{
				break;
			}
		}

		if (finish)
		{
			return t.step;
		}


		Node nn;

		for (i=0;i<n-1;++i)
		{
			memcpy(nn.state,t.state,sizeof(t.state));
			
			for(j=0;j<n;++j)
			{
				swap(nn.state[i][j],nn.state[i+1][j]);
			}
			
			nn.step=t.step+1;

			if (qurey(nn.state)==-1)
			{
				insert(nn.state);
				q.push(nn);
			}
		}
	}
		
}

int main()
{
	int T;
	freopen("A.in","r",stdin);
	freopen("As.txt","w",stdout);
	scanf("%d",&T);

	int i,j;

	int b=1;
	while (T--)
	{
		
		scanf("%d",&n);

		init();

		gets(key);

		memset(st.state,0,sizeof(st.state));

		for (i=0;i<n;++i)
		{
			gets(key);

			for (j=0;key[j]!='\0';++j)
			{
				st.state[i][j]=key[j]-'0';
			}
		}

		st.step=0;


		printf("Case #%d: %d\n",b++,Bfs());

	}

	return 0;
}