#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <set>

using namespace std;

int main()
{
    int T;
    //freopen("C-large.in","r",stdin);
    //freopen("date.out","w",stdout);
    scanf("%d", &T);
    for(int i=0;i<T;i++)
    {
	int A;
	int B;
	int num=0;
	cin >> A >> B;
	for(int j=A;j<=B;j++)
	{
	    set<int> sl;
	    char ch[20];
	    sprintf(ch,"%d",j);
	    string str = ch;
	    int length = str.length();
	    int m;
	    int n;
	    int s = j;
	    for(int l=0;l<length;l++)
	    {
		m = s/10;
		n = s%10;
		s =(int)(n*pow(10.0,(length-1)*1.0))+m;
		if(s>j&&s<=B&&sl.find(s)==sl.end()) {
		    sl.insert(s);
		    num++;
		}
	    }
	}

	cout << "Case #" << i+1 <<": "<<num<<endl;
    }
    //fclose(stdout);
    //fclose(stdin);
    return 0;
}
