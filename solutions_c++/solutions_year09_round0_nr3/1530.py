#include<stdio.h>
#include<vector>
using namespace std;

struct aNode{
	int p;
	int no;
};

vector <aNode> v[19];

void XYZ(){
    #ifndef  ONLINE_JUDGE
    freopen("C-large.in","r",stdin);
    #endif
}

int main()
{
	XYZ();
	FILE * cfPtr;
	cfPtr = fopen("out.txt","w");
	char letter[511];
	int n;
	int k;
	int i,j;
	int x,y;
	char word[]={"welcome to code jam"};
	scanf("%d",&n);
	aNode newNode;
	fgets(letter,510,stdin);
	int sum;
	for(k=1;k<=n;k++)
	{
		for(i=0;i<19;i++)
			v[i].clear();
		fgets(letter,510,stdin);
		i=0;
		while(letter[i]!=10 && letter[i]!='\0')
		{
			for(j=0;j<19;j++)
				if(letter[i] == word[j])
				{
					newNode.p = i;
					v[j].push_back(newNode);
				}
			i++;
		}
		for(i=0;i<v[18].size();i++)
			v[18][i].no = 1;
//			v[18][i].no = v[18].size() - i;
		for(i=17;i>=0;i--)
		{
			for(x=v[i+1].size()-2;x>=0;x--)
			{
				v[i+1][x].no += v[i+1][x+1].no;
				v[i+1][x].no %= 10000;
			}
			y=0;
			for(x=0;x<v[i].size();x++)
			{
				while(y<v[i+1].size() && v[i+1][y].p<=v[i][x].p)
					y++;
				if(y<v[i+1].size())
					v[i][x].no = v[i+1][y].no;
				else
					v[i][x].no = 0;
				int aa = v[i][x].no;
			}
		}
		sum = 0;
		for(i=0;i<v[0].size();i++)
		{
			sum+=v[0][i].no;
			sum%=10000;
		}
		if(sum<10)
			fprintf(cfPtr,"Case #%d: 000%d\n",k,sum);
		else if(sum<100)
			fprintf(cfPtr,"Case #%d: 00%d\n",k,sum);
		else if(sum<1000)
			fprintf(cfPtr,"Case #%d: 0%d\n",k,sum);
		else 
			fprintf(cfPtr,"Case #%d: %d\n",k,sum);

	}

	return 0;

}