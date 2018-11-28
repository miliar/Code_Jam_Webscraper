#include <iostream>
#include <string>
#include <map>
   
 int main()     {
	int t=0;
    std::string inp,inp2;
    std::map<char,char> m;

	m[' ']=' ';
	m['a']='y';
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';

	std::cin>>t;
	getline(std::cin, inp);
	for (int c=0;c<t; c++)
		{

			getline(std::cin, inp);
			std::string out="";
			std::string::const_iterator itr;
			for(int i=0; i<inp.size(); ++i){
				out+=m[inp.at(i)];
			}
			if (t!=0) printf("\n");
			std::cout<<"Case #"<<c+1<<": "<<out;
			//printf("Case #%d: %s",c+1, out.c_str() );

		}

		

          return 0;
        }