#include <iostream>
#include <string>

using namespace std;
using std::string;

int N;

const char text[] = "welcome to code jam"; 

string codejam = text;

int count(string s)
{
    int lstr;
    lstr = s.size();
    
    int counter[19][510];
    for(int k=0;k<19;k++)
	{
	    counter[k][0] = 0;
	}
    
    if(s[0]==codejam[0])
	{
	    counter[0][0] = 1;
	}


    for(int i=1;i<lstr;i++)
	{
	    if(s[i]==codejam[0])
		{
		    counter[0][i] = (counter[0][i-1] + 1)%10000;
		}	   
	    else
		{
		    counter[0][i] = counter[0][i-1];
		}
	    for(int j=1;j<19;j++)
		{
		    
		    if(s[i]==codejam[j])
			{
			    counter[j][i] = (counter[j][i-1] + counter[j-1][i-1])%10000;
			}
		    else
			{
			    counter[j][i] = counter[j][i-1];
			}
		}
	}

    return counter[18][lstr-1];
}


int main()
{   
    cin >> N;
    string lost;
    getline(cin,lost);
    for(int i=1; i<=N; i++)
	{
	    string str;
	    getline(cin, str);
	    /* cout << str << endl; */
	    int ans;
	    ans = count(str);
	    cout << "Case #" << i << ": ";
	    
	    if(ans==0)
		{
		    cout << "0000" << endl;
		}
	    if(ans>=1 && ans < 10)
		{
		    cout << "000" << ans << endl;
		}
	    if(ans>=10 && ans < 100)
		{
		    cout << "00" << ans << endl;
		}
	    if(ans>=100 && ans < 1000)
		{
		    cout << "0" << ans << endl;
		}	   
	    if(ans>=1000 && ans < 10000)
		{
		    cout << ans << endl;
		}    
	}
}
