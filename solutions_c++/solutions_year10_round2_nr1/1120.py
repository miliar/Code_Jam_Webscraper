#include <iostream>
#include <sstream>
#include <set>
#include <vector>


int main ()
{
	int	numberOfCases	= 0;
	int	counter			= 0;
	
	std::cin >> numberOfCases;
	
	while (counter < numberOfCases) {
		int	result	= 0;
		int	n		= 0;
		int	m		= 0;
		std::set<std::string>	existingPaths;

		std::cin >> n;
		std::cin >> m;
		
		for (int i = 0; i < n; ++i) {
			std::string path;
			std::cin >> path;
			for (int j = 1; j <= path.length (); ++j) {
				if (path.length () != j && path[j] != '/')
					continue;
				
				std::string subPath = path.substr (0, j);
				if (existingPaths.find (subPath) == existingPaths.end ())
					existingPaths.insert (subPath);
			}
		}

		for (int i = 0; i < m; ++i) {
			std::string newPath;
			std::cin >> newPath;

			for (int j = 1; j <= newPath.length (); ++j) {
				if (newPath.length () != j && newPath[j] != '/')
					continue;
				
				std::string subPath = newPath.substr (0, j);
				if (existingPaths.find (subPath) == existingPaths.end ()) {
					existingPaths.insert (subPath);
					++result;
				}
			}
		}

		std::cout << "Case #" << ++counter << ": " << result << std::endl;
	}
}