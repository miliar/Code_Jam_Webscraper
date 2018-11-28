#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector <string> inp;

int l, d, t;
string data[5001];

int doCnt(int, int, int);

int main(void)
{
	cin>>l>>d>>t;

	for(int i=0;i<d;i++) cin>>data[i];

	sort(data, data+d);

	inp.resize(l);


	for(int caseN=1;caseN<=t;caseN++)
	{
		int ans=0;
		string temp;
		cin>>temp;

		int ind=0;
		for(int i=0;i<l;i++)
		{
			inp[i]="";
			if(temp[ind]!='(') { inp[i]+=temp[ind++]; }
			else
			{
				ind++;
				while(temp[ind]!=')') inp[i]+=temp[ind++];
				ind++;
			}
		}

		ans=doCnt(0, d, 0);

		cout<<"Case #"<<caseN<<": "<<ans<<endl;
	}

	return 0;
}

int doCnt(int s, int e, int nth)
{
//	printf("called : %d %d %d\n", s, e, nth);
	if(s>=e) return 0;
	if(nth==l) { /*cout<<"ret : "<<max(0, e-s)<<endl;*/ return max(0, e-s); }

	int ret=0, mid, start, end, tempLoc[2];

	for(int i=0;i<inp[nth].size();i++)
	{
		tempLoc[0]=d-1, tempLoc[1]=0;
		start=s, end=e;
		while(start<end)
		{	
			mid=(start+end)/2;
			if(data[mid][nth]>inp[nth][i]) end=mid;
			else if (data[mid][nth]==inp[nth][i]) { tempLoc[0]=min(tempLoc[0], mid); end=mid; }
			else start=mid+1;
		}

		start=s, end=e;
		while(start<end)
		{	
			mid=(start+end)/2;
			if(data[mid][nth]>inp[nth][i]) end=mid;
			else if (data[mid][nth]==inp[nth][i]) { tempLoc[1]=max(mid, tempLoc[1]); start=mid+1; }
			else start=mid+1;
		}

//		printf("s e nth inp[nth][i] range : %d %d %d %c %d %d\n", s, e, nth, inp[nth][i], tempLoc[0], tempLoc[1]);


		if(data[tempLoc[0]][nth]==inp[nth][i] && data[tempLoc[1]][nth]==inp[nth][i]) ret+=doCnt(tempLoc[0], tempLoc[1]+1, nth+1);
	}

	return ret;
}
