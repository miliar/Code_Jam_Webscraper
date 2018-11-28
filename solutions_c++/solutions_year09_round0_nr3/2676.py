#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;
int r;

void test(const string& str1,const string& str2)
{
    if(str2.size()==0)
        r++;
    if(str1.size()==0)
        return;
    int temp = -1;
    while(1)
    {
        temp = str1.find(*(str2.begin()),temp+1);  
        if(temp == -1)
            return;
        else
            test(str1.substr(temp+1),str2.substr(1));
    }
}

int main()
{
    int n;
    cin>>n;
    getchar();
    for(int i = 1;i<=n;i++)
    {
        r = 0;
        char arr[41];
        cin.getline(arr,40,'\n');
        string temp(arr);
        
        test(temp,"welcome to code jam");
        cout<<"Case #"<<i<<": "<<setw(4)<<setfill('0')<<r<<endl;
    }
    return 0;
}
