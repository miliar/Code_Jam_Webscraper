#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
int w[501],cw;
int e[501],ce;
int l[501],cl;
int c[501],cc;
int o[501],co;
int m[501],cm;
int b_[501],cb_;
int t[501],ct;
int d[501],cd;
int j[501],cj;
int a[501],ca;

int func_ex(int n);
int func_lx(int n);
int func_cx(int n);
int func_ox(int n);
int func_mx(int n);
int func_ey(int n);
int func_b_x(int n);
int func_tx(int n);
int func_oy(int n);
int func_b_y(int n);
int func_cy(int n);
int func_oz(int n);
int func_dx(int n);
int func_ez(int n);
int func_b_z(int n);
int func_jx(int n);
int func_ax(int n);
int func_my(int n);


int main()
{
int n;
int i;

freopen("C:\\Temp\\inpu.txt","rt",stdin);
freopen("C:\\Temp\\output.txt","wt",stdout);
scanf("%d\n",&n);
char temp[501];
int case_n=1;
while(case_n<=n)
{
cw=0;
ce=0;
cl=0;
cc=0;
co=0;
cm=0;
cb_=0;
ct=0;
cd=0;
cj=0;
ca=0;

cin.getline(temp,501,'\n');
i=0;
while(temp[i]!='\0')
{
if(temp[i]=='w')
{
w[cw]=i;
cw++;                
}//end of if
else if(temp[i]=='e')
{
e[ce]=i;
ce++;                
}//end of if
else if(temp[i]=='l')
{
l[cl]=i;
cl++;                
}//end of if
else if(temp[i]=='c')
{
c[cc]=i;
cc++;                
}//end of if
else if(temp[i]=='o')
{
o[co]=i;
co++;                
}//end of if
else if(temp[i]=='m')
{
m[cm]=i;
cm++;                
}//end of if
else if(temp[i]==' ')
{
b_[cb_]=i;
cb_++;                
}//end of if
else if(temp[i]=='t')
{
t[ct]=i;
ct++;                
}//end of if
else if(temp[i]=='d')
{
d[cd]=i;
cd++;                
}//end of if
else if(temp[i]=='j')
{
j[cj]=i;
cj++;                
}//end of if
else if(temp[i]=='a')
{
a[ca]=i;
ca++;                
}//end of if
i++;
}// end of while(temp[i]!='\0')
int ans=0;
for(int k=0;k<cw;k++)
{ans+=func_ex(w[k]);
ans%=10000;
}
cout<<"Case #"<<case_n<<": "<<right<<setw(4)<<setfill('0')<<ans<<"\n";
case_n++;
}// while(case_n<=n)
return 0;   
}

int func_ex(int n)
{
int ans=0;
for(int i=0;i<ce;i++)
{
if(e[i]>n)
{ans+=func_lx(e[i]);
ans%=10000;
}
}
return ans;
}

int func_lx(int n)
{
    int ans=0;
for(int i=0;i<cl;i++)
{
if(l[i]>n)
{ans+=func_cx(l[i]);
ans%=10000;
}
}
return ans;
}

int func_cx(int n)
{
int ans=0;
for(int i=0;i<cc;i++)
{
if(c[i]>n)
{
ans+=func_ox(c[i]);
ans%=10000;}
}
return ans;
}

int func_ox(int n)
{
int ans =0;
for(int i=0;i<co;i++)
{
if(o[i]>n)
{
ans+=func_mx(o[i]);
ans%=10000;
}
}
return ans;
}

int func_mx(int n)
{
int ans=0;
for(int i=0;i<cm;i++)
{
if(m[i]>n)
{ans+=func_ey(m[i]);
ans%=10000;}
}
return ans;
}

int func_ey(int n)
{
int ans=0;
for(int i=0;i<ce;i++)
{
if(e[i]>n)
{ans+=func_b_x(e[i]);
ans%=10000;}
}
return ans;
}

int func_b_x(int n)
{
int ans=0;
for(int i=0;i<cb_;i++)
{
if(b_[i]>n)
{ans+=func_tx(b_[i]);
ans%=10000;}
}
return ans;
}

int func_tx(int n)
{
int ans=0;
for(int i=0;i<ct;i++)
{
if(t[i]>n)
{ans+=func_oy(t[i]);
ans%=10000;}
}
return ans;
}

int func_oy(int n)
{
int ans=0;
for(int i=0;i<co;i++)
{
if(o[i]>n)
{ans+=func_b_y(o[i]);
ans%=10000;}
}
return ans;
}

int func_b_y(int n)
{
int ans=0;
for(int i=0;i<cb_;i++)
{
if(b_[i]>n)
{ans+=func_cy(b_[i]);
ans%=10000;}
}
return ans;
}

int func_cy(int n)
{
int ans=0;
for(int i=0;i<cc;i++)
{
if(c[i]>n)
{ans+=func_oz(c[i]);
ans%=10000;}
}
return ans;
}

int func_oz(int n)
{
int ans=0;
for(int i=0;i<co;i++)
{
if(o[i]>n)
{ans+=func_dx(o[i]);
ans%=10000;}

}
return ans;
}
int func_dx(int n)
{
int ans=0;
for(int i=0;i<cd;i++)
{
if(d[i]>n)
{ans+=func_ez(d[i]);
ans%=10000;}
}
return ans;
}

int func_ez(int n)
{
int ans=0;
for(int i=0;i<ce;i++)
{
if(e[i]>n)
{ans+=func_b_z(e[i]);
ans%=10000;}
}
return ans;
}

int func_b_z(int n)
{
int ans=0;
for(int i=0;i<cb_;i++)
{
if(b_[i]>n)
{ans+=func_jx(b_[i]);
ans%=10000;}
}
return ans;
}

int func_jx(int n)
{
int ans=0;
for(int i=0;i<cj;i++)
{
if(j[i]>n)
{ans+=func_ax(j[i]);
ans%=10000;}
}
return ans;
}

int func_ax(int n)
{
int ans=0;
for(int i=0;i<ca;i++)
{
if(a[i]>n)
{ans+=func_my(a[i]);
ans%=10000;}
}
return ans;
}

int func_my(int n)
{
int ans=0;
for(int i=0;i<cm;i++)
{
if(m[i]>n)
ans++;
}
return ans;
}

