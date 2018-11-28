class City
{
public:
	City(int id, string name);
	int addRoads(int id, int sc, int ec, int c);
	void sort();
	typedef vector<Roads> Routes;
	
private:
	int cid;
	string name;
	vector<Roads> adjent;
	int minicost;
	vector<Routes> routes;
};

int solve( vector<City>& cityList )
{
	queue<int> reach;
	
	reach.push(0);
	
	while( !reach.empty() )
	{
		int city = reach.front();
		reach.pop();
		
		for(int i = 0; i < cityList[city].adjent.size(); i++)
		{
			int next = routes.endCity;
			
			if (cityList[next].reachable == 0)
			{
				reach.push( next );
				cityList[next].reachable = 1;
			}
			
			if( cityList[next].minicost >= cityList[city].minicost + cityList[city].adjent[i].cost
				|| cityList[next].minicost == 0 )
			{
				if ( cityList[next].minicost > cityList[city].minicost + cityList[city].adjent[i].cost )
				{
					cityList[next].routes.clear();
				}
				if( cityList[city].routes.size() > 0 )
					for(int j = 0; j < cityList[city].routes.size(); j++)
					{
						vector<Roads> r(cityList[city].routes[j]);
						r.push_back( cityList[city].adjent[i] );
						cityList[next].routes.push_back( r );
					}
				else
				{
					vector<Roads> r.push_back( cityList[city].adjent[i] );
					cityList[next].routes.push_back( r );
				}	
			}
		    else
		    {
		    	// do nothing
		    }
		}
	}
	return 0;
}