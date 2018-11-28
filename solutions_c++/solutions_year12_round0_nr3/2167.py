#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	ifstream infile;
	ofstream outfile;
        int T,A,B,count=0,num1,num2,temp_num,r;
	infile.open("Input.txt", ios::in);
	outfile.open("Output.txt", ios::out);

        infile>>T;
        for (r=0;r<T;r++)
        {
            infile>>A>>B;
            if (A<10)
            {
                count=0;
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<100)
            {
                count=0;
                num1=A;
                for (int i=A;i<=B;i++)
                {
                    int x,y;
                    x=num1/10;
                    y=num1%10;
                    num2=y*10+x;
                    if ((num2>=A) && (num2<=B) && (num1<num2))
                    {
                        count++;
                    }
                    num1++;
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<1000)
            {
                num1=A;
                count=0;
                for (int i=A;i<=B;i++)
                {
                    int x,y,z;
                    temp_num=num1;
                    do 
                    {
                        x=temp_num/100;
                        y=temp_num%100;
                        y=y/10;
                        z=temp_num%10;
                        temp_num=z*100+x*10+y;
                        if ((temp_num>=A) && (temp_num<=B) && (num1<temp_num))
                        {
                             count++;
                        }
                    }
                    while (temp_num!=num1);
                    num1++;
                    
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<10000)
            {
                num1=A;
                count=0;
                for (int i=A;i<=B;i++)
                {
                    int x,y,z,w;
                    temp_num=num1;
                    do 
                    {
                        x=temp_num/1000;
                        y=temp_num%1000;
                        y=y/100;
                        z=temp_num%100;
                        z=z/10;
                        w=temp_num%10;
                        temp_num=w*1000+x*100+y*10+z;
                        if ((temp_num>=A) && (temp_num<=B) && (num1<temp_num))
                        {
                             count++;
                        }
                    }
                    while (temp_num!=num1);
                    num1++;
                    
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<100000)
            {
                num1=A;
                count=0;
                for (int i=A;i<=B;i++)
                {
                    int x,y,z,w,a;
                    temp_num=num1;
                    do 
                    {
                        x=temp_num/10000;
                        y=temp_num%10000;
                        y=y/1000;
                        z=temp_num%1000;
                        z=z/100;
                        w=temp_num%100;
                        w=w/10;
                        a=temp_num%10;
                        temp_num=a*10000+x*1000+y*100+z*10+w;
                        if ((temp_num>=A) && (temp_num<=B) && (num1<temp_num))
                        {
                             count++;
                        }
                    }
                    while (temp_num!=num1);
                    num1++;
                    
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<1000000)
            {
                num1=A;
                count=0;
                for (int i=A;i<=B;i++)
                {
                    int x,y,z,w,a,b;
                    temp_num=num1;
                    do 
                    {
                        x=temp_num/100000;
                        y=temp_num%100000;
                        y=y/10000;
                        z=temp_num%10000;
                        z=z/1000;
                        w=temp_num%1000;
                        w=w/100;
                        a=temp_num%100;
                        a=a/10;
                        b=temp_num%10;
                        temp_num=b*100000+x*10000+y*1000+z*100+w*10+a;
                        if ((temp_num>=A) && (temp_num<=B) && (num1<temp_num))
                        {
                             count++;
                        }
                    }
                    while (temp_num!=num1);
                    num1++;
                    
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
            else if (A<10000000)
            {
                num1=A;
                count=0;
                for (int i=A;i<=B;i++)
                {
                    int x,y,z,w,a,b,c;
                    temp_num=num1;
                    do 
                    {
                        x=temp_num/1000000;
                        y=temp_num%1000000;
                        y=y/100000;
                        z=temp_num%100000;
                        z=z/10000;
                        w=temp_num%10000;
                        w=w/1000;
                        a=temp_num%1000;
                        a=a/100;
                        b=temp_num%100;
                        b=b/10;
                        c=temp_num%10;
                        temp_num=c*1000000+x*100000+y*10000+z*1000+w*100+a*10+b;
                        if ((temp_num>=A) && (temp_num<=B) && (num1<temp_num))
                        {
                             count++;
                        }
                    }
                    while (temp_num!=num1);
                    num1++;
                    
                }
                outfile<<"Case #"<<r+1<<": "<<count;
                if (T-1!=r)
                        outfile<<endl;
            }
        }
        
	infile.close();
	outfile.close();
        return 0;
}

