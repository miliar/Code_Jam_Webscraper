#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("data.out","w",stdout);

    int T;
    int S;
    int p;
    int N;
    string aa;
    getline(cin,aa);
    T = atoi(aa.c_str());
    for(int i=0;i<T;i++)
    {
	int num=0;
	int count =0;
	int temp=0;
	cin >> N >> S >> p;
	for(int j=0;j<N;j++)
	{
	    cin >> num;
	    if((3*p-4)<=num&&(3*p-2)>num&&num>=2)
		temp++;
	    if((3*p-2)<=num)
		count++;
	}
	if(temp>=S)
	    count += S;
	else
	    count += temp;
	cout <<"Case #"<<i+1<<": "<< count <<endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
