#include <iostream>

using namespace std;

int main()
{

    string a[100];
    int x;
    cout <<"input number of try : "; cin >>x;

    for(int j=0;j<x+1;)
   {getline(cin,a[j]);

    for(int i=0;i<a[j].length();i++)
    {
        if(a[j].substr(i,1)=="y")
        {a[j].replace(i,1,"a");}
        else if(a[j].substr(i,1)=="n")
        {a[j].replace(i,1,"b");}
        else if(a[j].substr(i,1)=="f")
        {a[j].replace(i,1,"c");}
        else if(a[j].substr(i,1)=="i")
        {a[j].replace(i,1,"d");}
        else if(a[j].substr(i,1)=="c")
        {a[j].replace(i,1,"e");}
        else if(a[j].substr(i,1)=="w")
        {a[j].replace(i,1,"f");}
        else if(a[j].substr(i,1)=="l")
        {a[j].replace(i,1,"g");}
        else if(a[j].substr(i,1)=="b")
        {a[j].replace(i,1,"h");}
        else if(a[j].substr(i,1)=="k")
        {a[j].replace(i,1,"i");}
        else if(a[j].substr(i,1)=="u")
        {a[j].replace(i,1,"j");}
        else if(a[j].substr(i,1)=="o")
        {a[j].replace(i,1,"k");}
        else if(a[j].substr(i,1)=="m")
        {a[j].replace(i,1,"l");}
        else if(a[j].substr(i,1)=="x")
        {a[j].replace(i,1,"m");}
        else if(a[j].substr(i,1)=="s")
        {a[j].replace(i,1,"n");}
        else if(a[j].substr(i,1)=="e")
        {a[j].replace(i,1,"o");}
        else if(a[j].substr(i,1)=="v")
        {a[j].replace(i,1,"p");}
        else if(a[j].substr(i,1)=="z")
        {a[j].replace(i,1,"q");}
        else if(a[j].substr(i,1)=="p")
        {a[j].replace(i,1,"r");}
        else if(a[j].substr(i,1)=="d")
        {a[j].replace(i,1,"s");}
        else if(a[j].substr(i,1)=="r")
        {a[j].replace(i,1,"t");}
        else if(a[j].substr(i,1)=="j")
        {a[j].replace(i,1,"u");}
        else if(a[j].substr(i,1)=="g")
        {a[j].replace(i,1,"v");}
        else if(a[j].substr(i,1)=="t")
        {a[j].replace(i,1,"w");}
        else if(a[j].substr(i,1)=="h")
        {a[j].replace(i,1,"x");}
        else if(a[j].substr(i,1)=="a")
        {a[j].replace(i,1,"y");}
        else if(a[j].substr(i,1)=="q")
        {a[j].replace(i,1,"z");}

    }
    cout <<endl;
    j++;
   }

    for(int j=0;j<x+1;j++)
   {cout <<" "<<a[j];}

    return 0;
}
