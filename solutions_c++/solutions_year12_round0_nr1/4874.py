#include<iostream>
#include<string>
#include <sstream>
using namespace std;
int main()
{
    
	int num,caseno=1,len;
	
    string mystr="";
    string input="";
    char ch;
	char arr1[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char arr2[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	while (true) {
    
    getline(cin, input);

    // This code converts from string to number safely.
    stringstream myStream(input);
    if (myStream >> num)
     break;
    cout << "Invalid number, please try again" << endl;
 }
	while(num>0)
	{
        getline(cin, mystr);	
    	cout<<"Case #"<<caseno<<": ";
		caseno++;
         
		//cout<<mystr<<endl;
		len=mystr.length();
		for(int i=0;i<len;i++)
		{
            ch=mystr[i];
            if(ch==' ')
             cout<<" ";
             else
             {
                for(int j=0;j<26;j++)
        		{
        			if(ch==arr2[j])
        				cout<<arr1[j];
        		}
            }
        }
        cout<<endl;
        num=num-1;

	}

		
	return 0;
}
