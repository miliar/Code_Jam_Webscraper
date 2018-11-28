#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int arr[30];
bool used[30];
int nod;
int mini= 0;
int num = 0;
int curr = 0;
int minmin = 0;

void use(int a, int b , int count, int val)
{
    if (count == 0 ) { if ((val>num)&&(val<mini)) {mini = val;} return;}
    for (int i=a;i<b;i++)
        if (!used[i])
        {
            used[i] = true;
            use(a,b, count - 1,(val*10) + arr[i]);
            used[i] = false;
        }
}

int mix(int a,int b)
{
    num = 0;
    curr = 0;
    for (int i=nod-1; i>=b; i--)
        {
            curr*=10; curr+= arr[i];
        }
    for (int i=b-1; i>=a; i--)
        { num *= 10; num += arr[i]; curr*=10;} 
//    cout << curr << " " << num << endl;
    mini = 100000000;
    for (int i=0;i<30;i++)
    {   used[i] = false;    }
    use(a, b, b-a, 0);
//    cout << "ans:" << b << " " << curr+mini << endl;
    return curr+mini;
}

int main(void)
{
    string s;
    getline(cin,s);
    stringstream ss(s);
    int n;
    ss >> n;
    for (int i = 0; i<n; i++)
    {
        minmin = 100000000;
        getline(cin,s);
        nod = s.length();
        int ori ;
        stringstream sss(s);
        sss >> ori;
        for (int j=0; j<s.length(); j++)
        {
            arr[j] = s[s.length()-1-j]-'0';
        }
        for (int j=2; j<= nod; j++)
        {
            int temp = mix(0,j);
            if (temp<minmin) {minmin = temp;}
        }
        if (minmin == 100000000)
        {   int smallest = 10;
            int smallind = 0;
            for (int i=0;i<30;i++)
            {   used[i] = false;    }        
            for (int j=0;j<s.length();j++)
            {   if ((s[j]-'0' < smallest)&&(s[j]!='0')) {smallest = s[j]-'0'; smallind = j;}
            }
            used[smallind] = true;
            minmin = smallest * 10;
            for (int k=1; k<nod; k++)
            {               smallest = 10; 
                for (int j=0;j<s.length();j++)
                {   if ((s[j]-'0' < smallest)&&(!used[j])) {smallest = s[j]-'0'; smallind = j;}
                }
                used[smallind]=true;
                minmin*= 10; minmin+= smallest;
            }
        }
        cout << "Case #" << i+1 << ": " << minmin << endl;
    }
}
