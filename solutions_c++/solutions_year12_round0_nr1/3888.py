#include <string>
class GoogleTranslator
{
	public:
		GoogleTranslator();
		~GoogleTranslator();

		std::string translate(std::string line_in);
	private:
		std::string english;
		std::string googlerese;
};