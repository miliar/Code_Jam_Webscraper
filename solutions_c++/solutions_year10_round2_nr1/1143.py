#include <iostream>
#include <vector>

using namespace std;



class Directory
{
public:
    string name;
    string path;

    Directory()
        {
            name = "";
            path = "";
        }

    Directory(string name, string path)
        {
            this->name = name;
            this->path = path;
        }

    friend ostream& operator<<(ostream& out, Directory d)
        {
            out << d.path+", "+d.name;
            return out;
        }
};

ostream& operator<<(ostream& out, vector<Directory>& v)
{
    for(int i = 0; i < v.size(); i++)
    {
        if(i > 0)
            out << "; [" << v[i] << "]";
        else
            out << "[" << v[i] << "]";
    }
    out << endl;

    return out;
}


bool contains(string name, string path, vector<Directory>& dirs)
{
    for( unsigned int i = 0; i < dirs.size(); i++)
        if(dirs[i].path == path && dirs[i].name == name)

    return false;
}

bool contains2(string name, string path, vector<Directory>& dirs)
{
    for( unsigned int i = 0; i < dirs.size(); i++)
        if(dirs[i].path == path && dirs[i].name == name)
            return true;

    //cout << "path: " + path + ",   name: " + name +"\n";
    //cout << dirs << endl;

    return false;
}



int parseDirString(string path_name, vector<Directory>& dirs)
{
    if(path_name.find("/") == string::npos)
        return 0;
    int count = 0;
    string path = "/";
    string name = "";
    while(path_name.find("/") != string::npos)
    {
        //cout << path_name << endl;
        int pos = path_name.find("/");
        if(pos > 0)
        {
            path += path_name.substr(0,pos+1);
            path_name = path_name.substr(pos+1, path_name.size());
            if(path_name.find("/") != string::npos)
                name = path_name.substr(0, path_name.find("/"));
            else
                name = path_name;

            if(!contains(name, path, dirs))
            {
                dirs.push_back(Directory(name,path));
                count++;
            }
                
        }
        else
        {
            path_name = path_name.substr(1,path_name.size());
            if(path_name.find("/") != string::npos)
                name = path_name.substr(0, path_name.find("/"));
            else
                name = path_name;

            if(!contains(name, path, dirs))
            {
                dirs.push_back(Directory(name,path));
                count++;
            }
        }
    }

    return count;
}

int parseDirString2(string path_name, vector<Directory>& dirs)
{
    if(path_name.find("/") == string::npos)
        return 0;
    int count = 0;
    string path = "/";
    string name = "";
    while(path_name.find("/") != string::npos)
    {
        //cout << path_name << endl;
        int pos = path_name.find("/");
        if(pos > 0)
        {
            path += path_name.substr(0,pos+1);
            path_name = path_name.substr(pos+1, path_name.size());
            if(path_name.find("/") != string::npos)
                name = path_name.substr(0, path_name.find("/"));
            else
                name = path_name;

            if(!contains2(name, path, dirs))
            {
                dirs.push_back(Directory(name,path));
                count++;
            }
                
        }
        else
        {
            path_name = path_name.substr(1,path_name.size());
            if(path_name.find("/") != string::npos)
                name = path_name.substr(0, path_name.find("/"));
            else
                name = path_name;

            if(!contains2(name, path, dirs))
            {
                dirs.push_back(Directory(name,path));
                count++;
            }
        }
    }

    return count;
}

int main()
{
    
    int num_entries;
    string junk;
    
    cin >> num_entries;
    getline(cin, junk);
    for(int i = 0; i < num_entries; i++)
    {
        vector<Directory> dirs;
        int num_exist;
        int num_new;
        cin >> num_exist >> num_new;
        getline(cin, junk);

        string line;
        for(int j = 0; j < num_exist; j++)
        {
            getline(cin, line);
            parseDirString(line, dirs);
        }


        int count = 0;
        
        for(int j = 0; j < num_new; j++)
        {
            getline(cin, line);
            count += parseDirString2(line, dirs);
        }

        cout << "Case #" << i+1 << ": " << count << endl;;
    }

    
    
    return 0;
}
