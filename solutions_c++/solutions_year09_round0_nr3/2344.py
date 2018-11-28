#include<iostream>
#include<cstring>
#include<set>
using namespace std;
static int result=0;
static string nowget;
const string target="welcome to code jam";
const int tar_len=strlen("welcome to code jam");
int findsub(string test,int len,int test_th,int tar_th);
int main()
{
    int M;
    cin >> M;
    string test;
    char testch[500];
    int len;
	cin.ignore();
    for(int i=0;i<M;i++)
    {
        for(int j=0;j<500;j++)
            testch[j]=0;
        len=0;


        cin.getline(testch,500,'\n');
        test=testch;
        result=0;
		len=test.length();
        findsub(test,len,0,0);
        cout<<"Case #"<<i+1<<": "<<result%10000/1000<<result%1000/100<<result%100/10<<result%10<<endl;
    }
	return 0;
}

int findsub(string test,int len,int test_th,int tar_th)
{
    if(len-test_th<tar_len-tar_th)
        return 0;
    if(tar_th==tar_len)
		return ++result;
    //for(int i=test_th; i < len ; i++ )
    //{
        if(test.at(test_th)==target.at(tar_th))
            findsub(test,len,test_th+1,tar_th+1);
        findsub(test,len,test_th+1,tar_th);
   // }
    return 0;
}
