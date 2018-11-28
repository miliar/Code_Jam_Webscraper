// Recycle nUM.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<conio.h>
#include<string>
#include<stdlib.h>
#include<fstream>
#include<map>
#include<set>
using namespace std;
struct TestCase
{
       unsigned int a;
       unsigned int b;
       string strA;
       string strB;
};
//std::map<string,string> g_RecPair;
int main()
{
	
    ifstream in("C-small-attempt2.in",ios::in);
    if(in)
    {
          unsigned int _iNumTC;
          char arr[1024]={0};
          in.getline(arr,1024);
          _iNumTC = atoi(arr);
    //cin>>_iNumTC;
   
    TestCase * _TC = new TestCase[_iNumTC];
    for(unsigned int i=0;i<_iNumTC;i++)
    {
                //cin>>_TC[i].a;
                char ch =32;
                in.getline(arr,1024,ch);
                _TC[i].a = atoi(arr);
                
                char txt[1024]={0};
                sprintf(txt,"%d",_TC[i].a);
                _TC[i].strA=txt;
                char a='\n';
               in.getline(arr,1024,a);
               _TC[i].b = atoi(arr);
               // cin>>_TC[i].b;
                 sprintf(txt,"%d",_TC[i].b);
                _TC[i].strB=txt;
    }
	ofstream out("myoutput.txt",ios::out);
    for(unsigned int i=0;i<_iNumTC;i++)
	{
		unsigned int _iNumRecNum=0;
		/*
		if(_TC[i].a ==_TC[i].b)
		{
			//g_RecPair[_TC[i].strA]= _TC[i].strB;
			_iNumRecNum++;
			//cout<<_TC[i].a<<endl;
		}
		*/	
		for(unsigned int n=_TC[i].a;n<_TC[i].b;n++)
		{
			
			for(unsigned int m=_TC[i].b;m>n;m--)
			{
				string strn,strm;
				char myText[1024]={0};
				sprintf(myText,"%d",n);
				strn=myText;
				sprintf(myText,"%d",m);
				strm=myText;
				
				if( strn.length()!=strm.length())
				{
					continue;
				}
				std::set<string> uniqueVal;
				pair<set<string>::iterator,bool> ret;
				for(unsigned int j=0;j<strn.length();j++)
				{
					if(j==0)
					{
						if(strn==strm)
						{
							ret=uniqueVal.insert(strn);
							if(ret.second==true)
							_iNumRecNum++;
						//	cout<<strn<<endl;
							continue;
						}
					}
					string strnOriginal = strn;
					string strnCopy =strn;
					string strmCopy =strm;
				
					string substr = strnCopy.substr(strnCopy.length()-j,strnCopy.length());
					strnCopy.erase(strnCopy.length()-j,strnCopy.length());
					strnCopy.insert(0,substr);
					
					if(strnOriginal == strnCopy)
					{
						continue;
					}
					if((strnCopy==strmCopy) && (strnCopy.length()==strmCopy.length()) )
					{
						//cout<<strnCopy<<endl;
						ret=uniqueVal.insert(strnCopy);
							if(ret.second==true)
						_iNumRecNum++;
						//g_RecPair[strnCopy]=strmCopy;
					}
				}

			}
		}
		char text[1024]={0};
		
		if(out)
		{
			sprintf(text,"Case #%d: %d",i+1,_iNumRecNum);
			out.write(text,strlen(text));
			char ch='\n';
			out.write(&ch,1);
		}
		cout<<"Case #"<<i+1<<": "<<_iNumRecNum/*g_RecPair.size()*/<<endl;
	}
    
    
    }
    else
    {
        cout<<"Canot open input file";
    }
	getch();
	return 0;
}

