# include <iostream>
# include <vector>
# include <string>

using namespace std;

int main ()
{
    int l,d,n;
    vector <string> array;
    cin>>l>>d>>n;
    for (int i=0;i<d;i++)
    {
        string str;
        cin>>str;
        array.push_back (str);
    }
    //vector <string> values;
    for (int m=0;m<n;m++)
    {
        string str;
        cin>>str;
        int k=0;
        vector <vector <char> > array1;
        for (int j=0;j<l;j++)
        {
            if (str[k]=='(')
            {
                 k++;
                 vector <char> arr;
                 while (str[k]!=')')
                 {
                      arr.push_back (str[k]);
                      k++;
                 }
                 k++;
                 array1.push_back (arr);
            }
            else
            {
                 vector <char> arr;
                 arr.push_back (str[k]);
                 array1.push_back (arr);
                 k++;
            }
        }
        /*for (int f=0;f<array1.size ();f++)
        {
            for (int gg=0;gg<array1[f].size ();gg++)
            {
                cout<<array1[f][gg]<<" ";
            }
            cout<<endl;
        }*/        
        vector <string> run=array;
        /*for (int f=0;f<run.size ();f++)
        {
            cout<<run[f]<<endl;
        } */   
        vector <string> temp;
        for (int j=0;j<array1.size();j++)
        {
            temp.clear();
            for (int f=0;f<run.size();f++)
            {
                for (int gg=0;gg<array1[j].size();gg++)
                {
                    if (run[f][j]==array1[j][gg])
                    {
                         temp.push_back (run[f]);
                         break;
                    }
                }
            } 
            run=temp;
        }            
        cout<<"Case #"<<(m+1)<<": "<<run.size()<<endl;     
    }       
    return 0;      
}                                               
