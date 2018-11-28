/***************************************************************************
 *   Copyright (C) 2008 by Denis,,,   *
 *   denis@denis-desktop   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/


#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <fstream>
using namespace std;
int main(int argc, char *argv[])
{
ifstream in("in.txt");
ofstream out("out.txt");
int num;
in>>num;
for (int i=0;i<num;i++)
	{
		vector <int> s1,s2;
		int num1;
		in>>num1;
		for (int j=0;j<num1;j++)
		{
			int tempi;
			in>>tempi;
			s1.push_back(tempi);
		}
		for (int j=0;j<num1;j++)
		{
			int tempi;
			in>>tempi;
			s2.push_back(tempi);	
		}
		vector <int> sb1=s1,sb2=s2;
		long s=0,sum2=0,sum1=0;
		while (s1.size()!=0)
		{
			sum1=(*max_element(s1.begin(),s1.end()))*(*min_element(s2.begin(),s2.end()));
			sum2=(*max_element(s2.begin(),s2.end()))*(*min_element(s1.begin(),s1.end()));
			if (sum2>sum1)
			{
				s1.erase(max_element(s1.begin(),s1.end()));
				s2.erase(min_element(s2.begin(),s2.end()));		
				s+=sum1;
			}
			else
			{
				s2.erase(max_element(s2.begin(),s2.end()));
				s1.erase(min_element(s1.begin(),s1.end()));
				s+=sum2;
			}
		}
		out<<"Case #"<<i+1<<": "<<s<<endl;
		cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	
 }
