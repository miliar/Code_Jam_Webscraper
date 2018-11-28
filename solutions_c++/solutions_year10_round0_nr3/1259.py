#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


struct node
{
	int number;
	bool visited;
	int round;
	int value;
	int index;
	int total;
};

void preProcessing(vector<node> & v, int k)
{
	int len=v.size();
 	for(int i=0;i<v.size();i++)
	{
		v[i].visited=false;
		v[i].round=0;
		int t=v[i].number;
		int ind=i;
		int value=t;
		int preInd=ind;
		while(t<=k)
		{
			value=t;
			if(ind==len-1) ind=0;
			else ind++;
			if(preInd==ind) break;
			t+=v[ind].number;
		}
		v[i].value=value;
		v[i].index=ind;
	}
}

int moneyEarned(vector<node> & v, int k, int R)
{
	preProcessing(v,k);
	int total=0;
	int curInd=0;
	for(int i=0;i<R;i++)
	{
		if(v[curInd].visited==false)
		{
			v[curInd].total=total;
			total+=v[curInd].value;
			v[curInd].visited=true;
			v[curInd].round=i;
			curInd=v[curInd].index;
		}
		else
		{
			int cycle=i-v[curInd].round;
			int cycleValue=total-v[curInd].total;
			int roundLeft=R-i;
			int residue=(R-i)%cycle;
			int iteration=(R-i)/cycle;
			total+=cycleValue*iteration;
			for(int j=0;j<residue;j++)
			{
				total+=v[curInd].value;
				curInd=v[curInd].index;
			}
			break;
		}
	}
	return total;
}



int main()
{
	ifstream file("C-small-attempt0.in");
	ofstream out("output.txt");
	int T;
	file>>T;
	for(int i=0;i<T;i++)
	{
		int R,k,N;
		file>>R>>k>>N;
		vector<node> v(N);
		for(int j=0;j<N;j++)
		{
			file>>v[j].number;
		}
		out<<"Case #"<<i+1<<": "<<moneyEarned(v,k,R)<<endl;
	}
	return 1;
}