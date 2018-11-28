#include<iostream>
using namespace std;

string jam="welcome to code jam";
int cnt[19];
int N;

int sfind(char a, int i)
{
    while(i<19)
    {
	if(jam[i]==a)
	    return i;
	i++;
    }
    return i;
}

int main()
{
    cin>>N;
    
    int i,j;
    string input;

    getline(cin,input);

    for(int c=1; c<=N; c++)
    {
	for(i=0; i<19; i++)
	    cnt[i]=0;

	getline(cin, input);
	for(i=0; i<input.size(); i++)
	{
	    j=sfind(input[i],0);
	    while(j<19)
	    {
		if(j==0)
		    cnt[j] += 1;
		else
		    cnt[j] += cnt[j-1];
		cnt[j] %= 10000;
		j = sfind(input[i], j+1);
	    }
	}

	int n=cnt[18];
	cout<<"Case #"<<c<<": ";
	if(n<10)
	    cout<<0;
	if(n<100)
	    cout<<0;
	if(n<1000)
	    cout<<0;
	cout<<n<<endl;
    }
}
	    

		   
