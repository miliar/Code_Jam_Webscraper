
	#include <iostream>
	#include <string>
    #include <map>
	#include <vector>
	#include <cmath>
	#include <algorithm>
	using namespace std;


	class my_int
	{
		
		
		public:
		int curr_size;	
		vector <int> a;				
			/*Constructor*/
			my_int()
			{
				curr_size = 0;
			//	a.push_back(1);
			}	

			/*Destructor*/
			~my_int()
			{
			}

/////////////////////////////////////////////////////////////////////////////////////////////

			/*Increment Operator*/
			void operator++()
			{
				int flag = 1;
				int i=0;
				while((flag)&&(i<curr_size))
				{
					if ((a[i]+1)<10)
					{
						a[i] = a[i] + 1;
						flag = 0;
					}
					else
					{
						a[i] = 0;
					}
					i++;
				}
				if ((i>=curr_size)&&(flag))
				{
					a.push_back(1);
					curr_size++;
					flag = 0;
				}
			}

//////////////////////////////////////////////////////////////////////////////////////////////

			/*I/O Operator*/
			friend ostream& operator << (ostream &os, my_int n)
			{
				for (int i = n.curr_size-1; i >= 0; i--)
				{
					os<<n.a[i];
				}
				return os;
			}

//////////////////////////////////////////////////////////////////////////////////////////////

			/*Multiplication operator*/
			my_int operator * (int m)
			{
				int temp, left, carry = 0;
				int flag = 0;
				my_int l;
				for (int i = 0; i < curr_size; i++)
				{
					temp = a[i]*m+carry;
					if (temp > 9)				
					{
						left = temp%10;
						l.a.push_back(left);
						carry = temp/10;
						flag = 1;
					}
					else
					{
						l.a.push_back(temp);
						flag = 0;
						carry = 0;				/*No carry in this case. check for case like 8!*/
					}
					l.curr_size++;
				}

				if (flag)		/*final carry need to be taken care of*/
				{
					while (carry)
					{
						l.a.push_back(carry%10);
						carry = carry/10;
						l.curr_size++;
					}
				}
				return l;
			}

//////////////////////////////////////////////////////////////////////////////////////////////////

			/*Binary addition operator*/
			my_int operator+ (long int n)
			{
				vector <int> b;
				int smaller;
				int larger;
				my_int l;
				while (n)
				{
					b.push_back(n%10);
					n = n/10;
				}
				smaller = b.size()<curr_size?b.size():curr_size;
				larger = b.size()>curr_size?b.size():curr_size;
				for (int i = 0; i < smaller; i++)
				{
					l.a.push_back(a[i]+b[i]);

				}
				if (curr_size > b.size())
				{
					for (int i = smaller; i<larger; i++)
					{
						l.a.push_back(a[i]);
					}
				}
				else
				{
					for (int i = smaller; i<larger; i++)
					{
						l.a.push_back(b[i]);
					}
				}
				rectify(l.a);
				l.curr_size = l.a.size();
				return l;
			}


//////////////////////////////////////////////////////////////////////////////////////////////////////

			my_int operator+ (my_int n)
			{
				int smaller, larger;
				my_int l;
				smaller = n.curr_size<curr_size?n.curr_size:curr_size;
				larger = n.curr_size>curr_size?n.curr_size:curr_size;
				for (int i =0; i < smaller; i++)
				{
					l.a.push_back(a[i]+n.a[i]);
				}
				if (curr_size> n.curr_size)
				{
					for (int i = smaller; i < larger; i++)
					{
						l.a.push_back(a[i]);
					}
				}
				else
				{
					for (int i = smaller; i<larger; i++)
					{
						l.a.push_back(n.a[i]);
					}
				}
				rectify(l.a);
				l.curr_size = l.a.size();
				return l;
			}


///////////////////////////////modulo////////////////////////////////////////////////////////

		/*	long int operator% (long int a)
			{
								
			}*/

///////////////////////////////////////////////////////////////////////////////////////////////////
			
			void rectify(vector <int> &a)
			{
				if (!(a.empty()))
				{
				    int temp;
					for (int i =0 ; i < a.size()-1; i++)
					{
						if (a[i]>=10)
						{
							temp = a[i]/10;
							a[i] = a[i]%10;
							a[i+1] = a[i+1]+temp;
						}
					}
					if (a[i]>=10)
					{
						temp = a[i]/10;
						a[i] = a[i]%10;
						a.push_back(temp);
					}
				}
			}

////////////////////////////////////////////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////////////////////////////////////////

	};




	int main()
	{
	    int no_of_cases;
		int t1;
		int i;
		cin>>no_of_cases;
		t1 = no_of_cases;
		while(t1--)
		{
            map <char, int>table;
			map<char,int>::iterator it;
		    int curr_no=0;
			int flag = 0;
			string num;
			string ans="";
			cin>>num;
            table[num[0]] = 1;
            for (i=1; i<num.size(); i++)
			{
				if (table.find(num[i])==table.end())
				{
					if (flag==0)
					{
					    table[num[i]] = 0;
						curr_no=2;
						flag = 1;
					}
					else
					{
						table[num[i]]= curr_no;
					    curr_no++;
					}
				}
			}
			if (curr_no==0)
			{
			    curr_no=2;
			}
		//for ( it=table.begin() ; it != table.end(); it++ )
        //        cout << (*it).first << " => " << (*it).second << endl;
			my_int ans2;
			ans2.curr_size = num.size();
			for (i=0; i<num.size(); i++)
			{
			    ans = ans+(char)(table[num[i]]+'0');
			    ans2.a.push_back(table[num[i]]);
			}
			//cout<<ans<<"\n";
			//reverse(ans2.a.begin(), ans2.a.end());
			//cout<<ans2;
			my_int m;
			for (i=num.size()-1; i>=0; i--)
			{
			    m=m+(int)(table[num[i]]*pow((double)curr_no, (double)(num.size()-1-i)));
			}
            cout<<"Case #"<<no_of_cases-t1<<": "<< m<<"\n";
		}
		return 0;
	
	}