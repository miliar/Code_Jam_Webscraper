
#include "liar.h"

/*********************************************************
 Group
 
 **********************************************************/
Group::Group( )
: m_hashTable( )
{
	FillDictionary( );
}

void Group::FillDictionary( )
{
	string googlerese1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string english1 =    "our language is impossible to understand";
						 
	string googlerese2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string english2 = "there are twenty six factorial possibilities";
						 
	string googlerese3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string english3 = "so it is okay if you want to just give up";
	
	//'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'
	
	m_hashTable[ 'z' ] = 'q';	
	m_hashTable[ 'q' ] = 'z';
	
	
	for (int i = 0; i< googlerese1.size( ); ++i )
	{
		if( googlerese1[i] != ' ')
		{
			if( DoesExists( googlerese1[i] ) == false )
			{
				m_hashTable[ googlerese1[i] ] = english1[i];
			}
		}
	}
	
	for (int i = 0; i< googlerese2.size( ); ++i )
	{
		if( googlerese2[i] != ' ')
		{
			if( DoesExists( googlerese2[i] ) == false )
			{
				m_hashTable[ googlerese2[i] ] = english2[i];
			}
		}
	}
	
	for (int i = 0; i< googlerese3.size( ); ++i )
	{
		if( googlerese3[i] != ' ')
		{
			if( DoesExists( googlerese3[i] ) == false )
			{
				m_hashTable[ googlerese3[i] ] = english3[i];
				
			}
		}
	}
	
}

string Group::GoogleErseToEnglish( string googleErse )
{
	
	string returnString;
	
	//cout << googleErse << "\n";
	for (int i = 0; i < googleErse.size( );  ++i )
	{
		map<char,char>::iterator it = m_hashTable.find( googleErse[i] );
		
		//cout << googleErse[i];
		
		if( it == m_hashTable.end( )  )
		{
			if( googleErse[i] == ' ')
			{
				returnString += " ";
			}
			else
			{
				//element not in table
				//returnString += "*";
				cout << "NOT IN DICT" << googleErse[i] << "\n";
			}			
		}
		else
		{
			returnString += it->second;
		}
	}
	return returnString;
}

bool Group::DoesExists( char toFindName )
{
	map<char,char>::iterator it;
	
	it = m_hashTable.find( toFindName );
	
	if( it == m_hashTable.end( )  )
	{
		return false;
	}
	else 
	{
		return true;
	}
}



void Group::Insert( char toInsertName )
{
	m_hashTable[toInsertName] = 'a';
}


void Group::Print( )
{
	for ( map<char,char>::iterator it = m_hashTable.begin( ); 
		 it != m_hashTable.end( ); 
		 ++it )
	{
		std::cout<< it->first<<"\t" << it->second << "\n";
	}
}