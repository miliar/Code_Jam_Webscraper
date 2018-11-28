//      googlerese.cpp
//      
//      Copyright 2012 Ivan <ivan@ivan-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <string>

using namespace std;

char trad[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
void translate(string text, bool end) {
	string::iterator it;
	for ( it=text.begin() ; it < text.end(); it++ )
	    if (*it == ' '){
			 cout << ' ';
		 }else { 
			 cout << trad[((int) *it) - 97];
		 }
	if (end) cout << endl;
}

int main(int argc, char** argv)
{
	int cases;
	cin >> cases;
	string str;
	getline(cin,str);

	for(int i =1; i < cases + 1; i++) {
		getline(cin,str);
		cout << "Case #" << i << ": ";
	    translate(str,true);  
	}
	
	getline(cin,str);
    translate(str,false);
	
	return 0;
}


