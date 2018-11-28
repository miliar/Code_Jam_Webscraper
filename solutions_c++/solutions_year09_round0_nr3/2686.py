#include<iostream>
#include<string>
#include<fstream>


using namespace std;



int main()
{

ifstream infile;
ofstream outfile;

infile.open("input.txt");
outfile.open("output.txt");



cout << "ok" << endl;

int numberofcases;

infile >> numberofcases;

string test;
char x;

infile.get(x);


for ( int v=0; v < numberofcases; v++)
{  
cout << "ok2" << endl;
getline(infile, test);

int a = test.size();

int phrase[19];
int sphrase[19];

bool lex = true;

cout <<"a"<< endl;
 phrase[0] = 0;

for ( int h=0; h < a; h++)
{
if ( test[h] == 'w')
{
phrase[0] = h;
break;
}
}



cout <<"phrase0" << phrase[0] << endl;

cout <<"b"<< endl;
char q;

for ( int i=1; i < 19; i++)
{
switch(i)
{ 
case 1: q= 'e'; break;
case 2: q= 'l'; break;
case 3: q= 'c'; break;
case 4: q= 'o'; break;
case 5: q= 'm'; break;
case 6: q= 'e'; break;
case 7: q= ' '; break;
case 8: q= 't'; break;
case 9: q= 'o'; break;
case 10: q= ' '; break;
case 11: q= 'c'; break;
case 12: q= 'o'; break;
case 13: q= 'd'; break;
case 14: q= 'e'; break;
case 15: q= ' '; break;
case 16: q= 'j'; break;
case 17: q= 'a'; break;
case 18: q= 'm'; break;

}
cout <<"qw" << endl;
for ( phrase[i] = phrase[i-1]; phrase[i] < a; phrase[i]++)
{ cout <<"ad" << endl;
if ( test[phrase[i]] == q) 
{
cout <<"cd" << endl;
break;
}
}

}

for ( int p=0; p < 19; p++)
{ char l;
switch(p)
{ 
case 1: l= 'e'; break;
case 2: l= 'l'; break;
case 3: l= 'c'; break;
case 4: l= 'o'; break;
case 5: l= 'm'; break;
case 6: l= 'e'; break;
case 7: l= ' '; break;
case 8: l= 't'; break;
case 9: l= 'o'; break;
case 10: l= ' '; break;
case 11: l= 'c'; break;
case 12: l= 'o'; break;
case 13: l= 'd'; break;
case 14: l= 'e'; break;
case 15: l= ' '; break;
case 16: l= 'j'; break;
case 17: l= 'a'; break;
case 18: l= 'm'; break;
}

//cout << phrase[p] << endl;
sphrase[p] = phrase[p];

if ( ((phrase[p] == a-1) && ( test[a-1] != l)) || (phrase[p] == a))
lex = false;


}
cout << "ok3" << endl;
int counter1=0;
bool m;
do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{

do
{
m= false;
cout <<"test" << endl;
counter1++;

for ( int y=phrase[0]+1; y < phrase[1]; y++)
{


if( test[y] == 'w')
{
m = true;

phrase[0] = y;


break;
}
}

}while(m);

phrase[0] = sphrase[0];

m= false;

for ( int y=phrase[1]+1; y < phrase[2]; y++)
{
if( test[y] == 'e')
{
m = true;
phrase[1] = y;


break;
}
}

}while(m);

phrase[1] = sphrase[1];

m= false;

for ( int y=phrase[2]+1; y < phrase[3]; y++)
{
if( test[y] == 'l')
{
m = true;
phrase[2] = y;


break;
}
}

}while(m);

phrase[2] = sphrase[2];

m= false;

for ( int y=phrase[3]+1; y < phrase[4]; y++)
{
if( test[y] == 'c')
{
m = true;
phrase[3] = y;


break;
}
}

}while(m);

phrase[3] = sphrase[3];

m= false;

for ( int y=phrase[4]+1; y < phrase[5]; y++)
{
if( test[y] == 'o')
{
m = true;
phrase[4] = y;


break;
}
}

}while(m);

phrase[4] = sphrase[4];

m= false;

for ( int y=phrase[5]+1; y < phrase[6]; y++)
{
if( test[y] == 'm')
{
m = true;
phrase[5] = y;


break;
}
}

}while(m);

phrase[5] = sphrase[5];

m= false;

for ( int y=phrase[6]+1; y < phrase[7]; y++)
{
if( test[y] == 'e')
{
m = true;
phrase[6] = y;


break;
}
}

}while(m);

phrase[6] = sphrase[6];

m= false;

for ( int y=phrase[7]+1; y < phrase[8]; y++)
{
if( test[y] == ' ')
{
m = true;
phrase[7] = y;


break;
}
}

}while(m);

phrase[7] = sphrase[7];
m= false;

for ( int y=phrase[8]+1; y < phrase[9]; y++)
{
if( test[y] == 't')
{
m = true;
phrase[8] = y;


break;
}
}

}while(m);

phrase[8] = sphrase[8];

m= false;

for ( int y=phrase[9]+1; y < phrase[10]; y++)
{
if( test[y] == 'o')
{
m = true;
phrase[9] = y;


break;
}
}

}while(m);

phrase[9] = sphrase[9];

m= false;

for ( int y=phrase[10]+1; y < phrase[11]; y++)
{
if( test[y] == ' ')
{
m = true;
phrase[10] = y;


break;
}
}

}while(m);

phrase[10] = sphrase[10];

m= false;

for ( int y=phrase[11]+1; y < phrase[12]; y++)
{
if( test[y] == 'c')
{
m = true;
phrase[11] = y;


break;
}
}

}while(m);

phrase[11] = sphrase[11];

m= false;

for ( int y=phrase[12]+1; y < phrase[13]; y++)
{
if( test[y] == 'o')
{
m = true;
phrase[12] = y;


break;
}
}

}while(m);

phrase[12] = sphrase[12];

m= false;

for ( int y=phrase[13]+1; y < phrase[14]; y++)
{
if( test[y] == 'd')
{
m = true;
phrase[13] = y;


break;
}
}

}while(m);

phrase[13] = sphrase[13];

m = false;

for ( int y=phrase[14]+1; y < phrase[15]; y++)
{
if( test[y] == 'e')
{
m = true;
phrase[14] = y;


break;
}
}

}while(m);

phrase[14] = sphrase[14];

 m= false;

for ( int y=phrase[15]+1; y < phrase[16]; y++)
{
if( test[y] == ' ')
{
m = true;
phrase[15] = y;


break;
}
}

}while(m);

phrase[15] = sphrase[15];

 m= false;

for ( int y=phrase[16]+1; y < phrase[17]; y++)
{
if( test[y] == 'j')
{
m = true;
phrase[16] = y;

break;
}
}

}while(m);

phrase[16] = sphrase[16];

 m= false;

for ( int y=phrase[17]+1; y < phrase[18]; y++)
{
if( test[y] == 'a')
{
m = true;
phrase[17] = y;

break;
}
}

}while(m);

phrase[17] = sphrase[17];

 m= false;

for ( int y=phrase[18]+1; y < a; y++)
{
if( test[y] == 'm')
{
m = true;
phrase[18] = y;

break;
}
}

}while(m );



if (lex)
{
if ( counter1 < 10) 
{
outfile << "Case #" << v+1 <<": 000" << counter1 << endl; 
}

if ( (counter1 < 100) && ( counter1 >= 10))
{
outfile << "Case #" << v+1 <<": 00" << counter1 << endl; 
}

if ( (counter1 < 1000) &&( counter1 >= 100))
{
outfile << "Case #" << v+1 <<": 0" << counter1 << endl; 
}

if ( counter1 >= 1000)
{ 
counter1 = counter1%10000;
outfile << "Case #" << v+1 <<": " << counter1 << endl; 
}

}

else 
{
outfile << "Case #" << v+1 <<": " << "0000" << endl;  

}

}

return 0;
}




