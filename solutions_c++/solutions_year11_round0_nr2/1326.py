#include "iostream"
#include "string"

using namespace  std;

int n;
string com[100],ops[100],instr;
char res[200];
int c,d;

int point=0,len;

void checkCom()
{
	if(point<1)
		return;
	for(int i=0;i<c;++i)
	{
		if(res[point]==com[i][0] && res[point-1]==com[i][1] ||
			res[point]==com[i][1] && res[point-1]==com[i][0])
		{
			res[point-1]=com[i][2];
			point--;
			return;
		}
	}
}
void checkOps()
{
	if(point<1)
		return;
	for(int i=0;i<d;++i)
	{
		for(int j=0;j<point;++j)
		{
			if(res[point]==ops[i][0] && res[j]==ops[i][1] ||
				res[point]==ops[i][1] && res[j]==ops[i][0])
			{
				point=-1;
				return;
			}
		}
	}
}
void work()
{
	cin>>c;
	for(int i=0;i<c;++i)
		cin>>com[i];

	cin>>d;
	for(int i=0;i<d;++i)
	{
		cin>>ops[i];
	}
	cin>>instr>>instr;
//	cout<<instr<<endl;
	
	len=instr.size();
	point=-1;

	for(int i=0;i<len;++i)
	{
		point++;
		res[point]=instr[i];
		checkCom();
		checkOps();
//		for(int j=0;j<point;++j)
//			cout<<res[j]<<" ";
//		cout<<endl;
	}

	cout<<"[";
	for(int i=0;i<=point;++i)
	{
		cout<<res[i];
		if(i<point)
			cout<<", ";
	}
	cout<<"]"<<endl;
}

int main()
{
	freopen("b.txt","r",stdin);
	freopen("b.out.txt","w",stdout);

	int cs;
	cin>>cs;
	for(int i=1;i<=cs;++i)
	{
		cout<<"Case #"<<i<<": ";
		work();
	}
}