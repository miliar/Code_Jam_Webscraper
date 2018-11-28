#include <map>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

#undef min
#undef max

class AlphabetMap
{
public:
  AlphabetMap(const std::string& base,
              const std::string& coded)
  {
    unsigned int alphabet_length = static_cast<unsigned int>(std::min(base.size(), coded.size()));

    for (unsigned int i = 0; i < alphabet_length; ++i)
    {
      _coded_to_base[coded[i]] = base[i];
      _base_to_coded[base[i]] = coded[i];
    }
  }

  char code (char base_character)
  {
    std::map<char, char>::iterator i = _base_to_coded.find(base_character);

    if (i != _base_to_coded.end())
      return i->second;
    return 0;
  }

  char decode (char coded_character)
  {
    std::map<char, char>::iterator i = _coded_to_base.find(coded_character);

    if (i != _coded_to_base.end())
      return i->second;
    return 0;
  }

  std::string translate(const std::string& input_string)
  {
    std::string output_string;

    output_string.resize(input_string.size());
    for (unsigned int i = 0, size = static_cast<unsigned int>(input_string.size()); i < size; ++i)
      output_string[i] = decode(input_string[i]);
    return output_string;
  }

private:
  std::map<char, char> _coded_to_base;
  std::map<char, char> _base_to_coded;
};

int
main(int argc, char* argv[])
{
  if (argc < 2)
  {
    std::cerr << "[usage} ./a.out <filename>" << std::endl;
    return 1;
  }  

  AlphabetMap alphabet_map ("abcdefghijklmnopqrstuvwxyz ", "ynficwlbkuomxsevzpdrjgthaq ");
  int nb_entries = 0;
  std::ifstream input_file (argv[1]);
  

  if (!input_file.is_open())
    return 2;
  
  std::stringstream tmp;
  std::string line;

  if (!getline(input_file, line))
  {
    std::cerr << "Could not read number of cases." << std::endl;
    return 3;
  }
  tmp << line;
  tmp >> nb_entries;

  if (nb_entries < 0)
  {
    std::cerr << "Invalid number of entries." << std::endl;
    return 4;
  }  

  bool success = true;

  for (int i = 1; i <= nb_entries; ++i)
  {
    if (!getline(input_file, line))
    {
      std::cerr << "Unexpected EOF" << std::endl;
      return 5;
    }
    
    const std::string& decoded_string = alphabet_map.translate(line);

    if (decoded_string.size() < line.size())
    {
      std::cerr << "Unknown character encountered." << std::endl;
      success = false;      
    }
    std::cout << "Case #" << i << ": " << decoded_string << std::endl;
  }
  if (!success)
    return 5;
	return 0;
}
