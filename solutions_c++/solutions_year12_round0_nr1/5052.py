#include<iostream>

using namespace std;

int main()
{
    int T = 0;
    char ch[101];
    int i=0;
    int count = 1;
    cin >> T;    
    cin.get();
    while(T > 0)
    {   
        i = 0;
        cin.getline(ch,101);
        cout<<"Case #"<<count<<": ";
        while(ch[i] != '\0')
        {
            switch(ch[i] - 96)
            {
                case 1:
                cout<<'y';
                break;
                
                case 2:
                cout<<'h';
                break;
                
                case 3:
                cout<<'e';
                break;
                
                case 4:
                cout<<'s';
                break;
                
                case 5:
                cout<<'o';
                break;
                
                case 6:
                cout<<'c';
                break;
                
                case 7:
                cout<<'v';
                break;
                
                case 8:
                cout<<'x';
                break;
                
                case 9:
                cout<<'d';
                break;
                
                case 10:
                cout<<'u';
                break;
                
                case 11:
                cout<<'i';
                break;
                
                case 12:
                cout<<'g';
                break;
                
                case 13:
                cout<<'l';
                break;
                
                case 14:
                cout<<'b';
                break;
                
                case 15:
                cout<<'k';
                break;
                
                case 16:
                cout<<'r';
                break;
                
                case 17:
                cout<<'z';
                break;
                
                case 18:
                cout<<'t';
                break;
                
                case 19:
                cout<<'n';
                break;
                
                case 20:
                cout<<'w';
                break;
                
                case 21:
                cout<<'j';
                break;
                
                case 22:
                cout<<'p';
                break;
                
                case 23:
                cout<<'f';
                break;
                
                case 24:
                cout<<'m';
                break;
                
                case 25:
                cout<<'a';
                break;
                
                case 26:
                cout<<'q';
                break;   
                
                default:
                cout<<' '; 
                break;                           
            }
            i++;
        }
        cout<<endl;
        T--;
        count++;
    }
}
