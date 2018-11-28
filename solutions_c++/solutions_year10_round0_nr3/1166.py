#include<fstream>
using namespace std;
#define Int int
int main()
{
	ifstream fin("C-large.in");
	ofstream fout("1.out");
	int R,k,N,i,Case,M;
	fin>>M;
	int data[1100];
	Int Res[1100][2];
	Int sum;
	Int index[1100][2];
	for(Case=1;Case<=M;Case++)
	{
        sum=0;
		fin>>R>>k>>N;
		for(i=0;i<N;i++)
		{
			fin>>data[i];
			sum+=data[i];
		}
		if(sum<=k)
		{
                  fout<<"Case #"<<Case<<": "<<sum*R<<endl;
                  continue;
                  }
		Res[0][0]=0;
		for(i=0;i<N;i++)
		{
			int j=i;
			Res[i][0]=0;
			while(Res[i][0]+data[j]<=k)
			{
				Res[i][0]+=data[j];
				j++;
				if(j==N)j=0;
			}
			Res[i][1]=j;
			index[i][0]=-1;
		}
		Int res=0;
		Int now=0;
		for(i=0;i<R;i++)
		{
            if(index[now][0]==-1)
            {
            index[now][0]=res;
            index[now][1]=i;
			res+=Res[now][0];
			now=Res[now][1];
        }
        else
        {
            res+=((R-i)/(i-index[now][1]))*(res-index[now][0]);
            break;
        }
		}
		for(i=i+(R-i)/(i-index[now][1])*(i-index[now][1]);i<R;i++)
		{
            index[now][0]=1;
            index[now][1]=i;
			res+=Res[now][0];
			now=Res[now][1];
        }
//		for(i=0;i<N;i++)
//			fout<<Res[i][0]<<' '<<Res[i][1]<<endl;

		fout<<"Case #"<<Case<<": "<<res<<endl;
	}
	return 0;
}
