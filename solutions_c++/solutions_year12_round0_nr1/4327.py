#include<iostream>
#include<string>

using namespace std;

int main()
{
    string input,output;
    int charmap[200]={-1};
    for(int i=0;i<3;i++)
    {
        getline(cin,input);
        getline(cin,output);
        int x,y;
        for(int j=0;j<input.size();j++)
        {
            x=int(input[j]);
            y=int(output[j]);
            if(charmap[x]==0)
            {

                            charmap[x]=y;
      //          cout<<x<<" "<<y<<endl;
            }

            else
            {

                if(charmap[x]==y){}
                else
                    {
                        cout<<"Erronous mapping\n";
                    }
            }
        }

    }
    for(int i=97;i<97+26;i++)
    {
    //    cout<<char(i);
    }
    //cout<<endl;
    for(int i=97;i<97+26;i++)
    {
        cout<<char(charmap[i]);
    }
    return 0;

}




