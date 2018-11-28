#include <iostream>
#include <list>
#include <set>
#include <stdexcept>
#include <string>


using namespace std;


typedef set<string> EnginesNames;


class Engines
{
    public:

        int size;
        EnginesNames names;

        Engines(istream& stream) throw(exception)
        {
            load_from_stream(stream);
        }

        void load_from_stream(istream& stream) throw(exception)
        {
            names.clear();
            stream >> ws >> size;

            for(int i = 0; i < size; i++) {
                string name;
                stream >> ws;
                getline(stream, name, '\n');
                names.insert(name);
            }
        }
};


typedef list<string> InstancesNames;


class Instances
{
    public:

        int size;
        Engines& engines;
        InstancesNames names;

        Instances(Engines& engns, istream& stream) throw(exception) : engines(engns)
        {
            load_from_stream(stream);
        }

        void load_from_stream(istream& stream) throw(exception)
        {
            names.clear();
            stream >> ws >> size;

            for(int i = 0; i < size; i++) {
                string name;
                stream >> ws;
                getline(stream, name, '\n');
                names.push_back(*engines.names.find(name));
            }
        }
};


class Problem
{
    public:

        int size;

        Problem(istream& in, ostream& out) throw(exception)
        {
            in >> ws >> size;

            for(int i = 0; i < size; i++) {
                Engines engines(in);
                Instances instances(engines, in);
                out << "Case #" << (i + 1) << ": " << solve(engines, instances) << endl;
            }
        }

        int solve(Engines& engines, Instances& instances) throw()
        {
            int count = 0;
            EnginesNames names = engines.names;

            while(!instances.names.empty()) {
                names.erase(*instances.names.begin());

                if(names.empty()) {
                    names = engines.names;
                    names.erase(*instances.names.begin());
                    count++;
                }

                instances.names.pop_front();
            }

            return count;
        }
};

int main()
{
    Problem p(cin, cout);
}
