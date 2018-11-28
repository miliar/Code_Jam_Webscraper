/**
 *
 * /file a.cpp
 *
 * Contains the solution to the A problem from the Qualification Round of the Google Code Jam 2008.
 *
 * /author Dimitar Asenov
 * /date July 17, 2008
 */

#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	// Read the number of test cases.
	int n;
	cin>>n;

	for (int ni = 1; ni <=n; ++ni)
	{
		map< string, bool > servers;

		// Read in the servers.
		int s;
		cin>>s;
		cin.ignore();

		for (int si = 0 ; si < s ; ++si)
		{
			string server;
			getline (cin, server);
			servers[server] = false;
		}

		// Read the number of queries.
		int q;
		cin>>q;
		cin.ignore();

		int servers_passed = 0;
		int switches_needed = 0;

		// Process each query.
		for (int qi = 0; qi<q; ++qi)
		{
			string query;
			getline(cin, query);

			// If this is a server that we have not already passed, it should be handled.
			if ( servers.find( query ) != servers.end() && servers[query] == false)
			{
				// Mark this server as already considered.
				++servers_passed;
				servers[query] = true;

				// The deepest possible server is the switch point.
				if (servers_passed == s)
				{
					++switches_needed;
					servers_passed = 1;

					// Unmark all other servers to prepare for a new search.
					for (map< string, bool >::iterator sit = servers.begin(); sit!= servers.end(); ++sit)
						sit->second = false;
					servers[query] = true;
				}
			}
		}

		cout<<"Case #"<<ni<<": "<<switches_needed<<endl;

	}

	return 0;
}
