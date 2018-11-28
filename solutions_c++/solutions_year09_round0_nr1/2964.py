#include<iostream>
#include<vector>
#include<string>
#include<algorithm>


using namespace std;

int main()
{
//	cout << "It's working !!" << endl;
	int l,d,n;
	cin >> l >> d >> n;
	
    vector<string> word;
    string str;
	for(int i=0;i<d;i++)
	{
        cin >> str;
        word.push_back(str);
        str.clear();
    }
    
    vector<int> lnum;
    int ctr;
    bool flag = true;
    bool group = false;
    for(int i=0;i<n;i++)
	{
        ctr = 0;
        flag =true;
        group=false;
        cin >> str;
       // cout << str.length() << endl;
        if(int(str.length())!=l)
        {
            int p = 0;
            vector<string> temp;
            string t;
            for(int j=0;j<int(str.length());j++)
            {
                    if(str[j]=='(')
                    {
                   //     if(j!=0 && str[j-1]!=')')
                   //      {
                   //      temp.push_back(t);
                   //      t.clear();
                   //      }
                         group = true;
                         
                    }   
                    else if(str[j]==')')
                    {
                         temp.push_back(t);
                         t.clear();
                         group=false;
                    }
                    else
                    {
                        if(group)
                         t.push_back(str[j]);
                        else
                        {
                            t.push_back(str[j]);
                            temp.push_back(t);
                            t.clear();
                        }
                    }
            }
            if(t.size()!=0)
                temp.push_back(t);
            
       /*     cout << "got here 1" << endl;
            for(int j=0;j<l;j++)
            {
                cout << temp[j] << endl;        
            }
            cout << "got here 2" << endl;
         */   
            if(int(temp.size())==l)
            {
            for(int j=0;j<d;j++)
            {
                    flag = true;
                    for(int k=0;k<l;k++)
                    {
                            if(temp[k].find(word[j][k])!=-1)
                                 continue;
                            else
                            {
                                 flag =false;
                                 break;
                            }
                    }
                    if(flag) ctr++;
            }
            }
      //      cout << "got here 3 with ctr = " << ctr << endl;
            lnum.push_back(ctr);
        }
        else
        {
            for(int j=0;j<d;j++)
            {
                    if(equal(str.begin(),str.end(),word[j].begin()))
                         ctr = 1;
            }
      //      cout << ctr <<  endl;
            lnum.push_back(ctr);
        }
        
    }
    for(int i=0;i<n;i++)
	{
            cout << "Case #" << i+1 << ": " << lnum[i] ;
            if(i!=n-1)
               cout << endl;
    }
	return 0;
}
