#include <fstream>
#include <bitset>
#include <string>

using namespace std;

int n,m;

int mat[512][512];

bool sizes[512];
int cnt[512];
int maxsize=0;
int maxY,maxX;

void addLine(int line,char* text)
{
	int len = strlen(text);
	int nr[128];
	for(int i=0;i<len;i++)
	{
		if(text[i]>='0' && text[i]<='9')
			nr[i]=text[i]-'0';
		else
			nr[i]=10+text[i]-'A';
		bitset<4> b(nr[i]);
		b.flip();
		for(int y=i*4;y<i*4+4;y++)
		{
			mat[line][y]=(int)b[3-(y-i*4)];
		}
	}
	
	/*for(int i=0;i<n;i++)
	{
		mat[line][i]=(int)b[i];
	}*/
}

int sizefill(int X, int Y)
{
	if(mat[X][Y]==2)
		return 0;
	bool ok=true;
	//bool eroare=false;
	int row=0;
	int paritate;
	if(mat[X][Y]==1)
		paritate=1;
	else
		paritate=0;
	while(ok && (X+row)<n && (Y+row)<m)
	{
		row++;
		for(int i=0;i<=row;i++)
		{
			if((i+row)%2==1)
			{
				if(mat[X+row][Y+i]==!paritate)
				{
				} else {
					ok=false;
				}
				if(mat[X+i][Y+row]==!paritate)
				{
				} else {
					ok=false;
				}
			}else{
				if(mat[X+row][Y+i]==paritate)
				{
				} else {
					ok=false;
				}
				if(mat[X+i][Y+row]==paritate)
				{
				} else {
					ok=false;
				}
			}
		}
	}
	return row;
}

int main()
{
	ifstream f("C-large.in");
	ofstream f2("output.out");

	int T;
	f>>T;
	char line[128];
	long long int temp,REZ;
	for(int TEST=0;TEST<T;TEST++)
	{
		printf("%d \n",TEST);
		maxsize=-1;
		maxY=0;
		maxX=0;
		f>>n>>m;
		for(int i=0;i<512;i++)
		{
			sizes[i]=false;
			cnt[i]=0;
		}
		for(int i=0;i<n;i++)
		{
			f>>line;
			addLine(i,line);
		}

		//INTERM
		/*f2<<endl;
		for(int i=0;i<n;i++)
		{
			for(int y=0;y<m;y++)
				f2<<mat[i][y]<<" ";
			f2<<endl;
		}
		f2<<endl;*/
		//INTERM

		while(maxsize!=0 && maxsize!=1)
		{
			maxsize=-1;
			maxY=0;
			maxX=0;
			for(int i=0;i<n;i++)
			{
				for(int y=0;y<m;y++)
				{
					temp=sizefill(i,y);
					if(temp>maxsize)
					{
						maxsize=temp;
						maxX=i;
						maxY=y;
					}
				}
			}
			if(maxsize>-1)
			{
				sizes[maxsize]=true;
				cnt[maxsize]++;
				for(int i=maxX;i<maxX+maxsize;i++)
				{
					for(int y=maxY;y<maxY+maxsize;y++)
					{
						mat[i][y]=2;
					}
				}
			}
			
		}
		REZ=1;
		for(int i=2;i<=n;i++)
		{
			if(sizes[i])
				REZ++;
		}
		temp=0;
		for(int i=n;i>=2;i=i-1)
		{
			if(sizes[i])
			{
				//f2<<i<<" "<<cnt[i]<<endl;
				temp+=i*i*cnt[i];
			}
		}
		if(temp==n*m)
			REZ=REZ-1;
		f2<<"Case #"<<TEST+1<<": "<<REZ<<endl;
		
		temp=0;
		for(int i=n;i>=2;i=i-1)
		{
			if(sizes[i])
			{
				f2<<i<<" "<<cnt[i]<<endl;
				temp+=i*i*cnt[i];
			}
		}
		if(temp<n*m)
			f2<<1<<" "<<n*m-temp<<endl;
	}
	
	


	f.close();
	f2.close();
	return 0;
}
