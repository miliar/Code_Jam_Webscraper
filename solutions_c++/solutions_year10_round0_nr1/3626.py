#include<iostream>
#include<vector>

using namespace std;
int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.txt","w",stdout);
    int T, N , K ;
    cin >> T;

    vector<int> vvalues;
    vvalues.push_back(0);
    vvalues.push_back(2);
    int cal=2;
    for(int t=2;t<33;t++)
    {
    cal = cal*2;
    //cout << cal << endl;
    vvalues.push_back(cal);
    }
    for(int tnk=0;tnk<T;tnk++)
    {
    cin >> N >> K ;
    int value = vvalues[N];

    //cout << value << " Value" << endl;

    {
           if(value == K+1)
           cout << "Case #" << tnk+1 <<": ON" << endl;
           else if((K+1)%value==0)
           cout << "Case #" << tnk+1 <<": ON" << endl;
           else
           cout << "Case #" << tnk+1 <<": OFF" << endl;

    }
  }
}
